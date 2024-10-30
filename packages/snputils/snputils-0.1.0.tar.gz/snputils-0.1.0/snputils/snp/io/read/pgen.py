import logging
from typing import Optional

import numpy as np
import numpy.typing as npt
import pandas as pd
import pgenlib as pg
from joblib import Parallel, delayed
from tqdm import tqdm

from snputils.snp.genobj.snpobj import SNPObject
from snputils.snp.io.read.base import SNPBaseReader

log = logging.getLogger(__name__)


@SNPBaseReader.register
class PGENReader(SNPBaseReader):
    def read(
        self,
        sample_ids: Optional[np.ndarray] = None,
        sample_idxs: Optional[np.ndarray] = None,
        variant_ids: Optional[np.ndarray] = None,
        variant_idxs: Optional[np.ndarray] = None,
        phased: bool = True,
        n_jobs: int = 1,
    ) -> SNPObject:
        """
        Reads a pgen fileset (pgen, psam, pvar) into a SNPObject.

        Args:
            sample_ids: List of sample IDs to read. If None, all samples are read.
            sample_idxs: List of sample indices to read. If None, all samples are read.
            variant_ids: List of variant IDs to read. If None, all variants are read.
            variant_idxs: List of variant indices to read. If None, all variants are read.
            phased: Whether to read and store the genotypes as phased.
                Note that due to the pgenlib backend, when phased is True, 8 times as much RAM is required.
                Nonetheless, the calldata_gt will only be double the size.
            n_jobs: Number of jobs to use for parallel reading. -1 means all CPUs.
                Not used if phased is False, since parallel reading is not supported.

        Returns:
            snpobj: SNPObject containing the data from the pgen fileset.
                If phased is True, calldata_gt is stored as a numpy array of shape (num_variants, num_samples, 2) and dtype int8 containing 0, 1.
                If phased is False, calldata_gt is stored as a numpy array of shape (num_variants, num_samples) and dtype int8 containing 0, 1, 2.
        """
        assert (
            sample_idxs is None or sample_ids is None
        ), "Only one of sample_idxs and sample_ids can be specified"
        assert (
            variant_idxs is None or variant_ids is None
        ), "Only one of variant_idxs and variant_ids can be specified"

        filename_noext = str(self.filename)
        if filename_noext[-5:] == ".pgen":
            filename_noext = filename_noext[:-5]

        log.info(f"Reading {filename_noext}.pvar")

        pvar_has_header = True
        pvar_header_line_num = 0
        with open(filename_noext + ".pvar") as file:
            for line_num, line in enumerate(file):
                if line.startswith("#CHROM"):
                    pvar_header_line_num = line_num
                    break
            else:  # if no break
                pvar_has_header = False
        pvar = pd.read_csv(
            filename_noext + ".pvar",
            sep=r"\s+",
            skiprows=pvar_header_line_num,
            header="infer" if pvar_has_header else None,
            names=(
                None if pvar_has_header else ["#CHROM", "ID", "CM", "POS", "REF", "ALT"]
            ),
            dtype={
                "#CHROM": str,
                "POS": pd.Int64Dtype(),
                "ID": str,
                "REF": str,
                "ALT": str,
            },
        )
        file_num_variants = len(pvar.index)

        if variant_ids is not None:
            variant_idxs = np.array(pvar.index[pvar["ID"].isin(list(variant_ids))])

        if variant_idxs is None:
            num_variants = file_num_variants
            variant_idxs = np.arange(num_variants, dtype=np.uint32)
        else:
            num_variants = np.size(variant_idxs)
            variant_idxs = np.array(variant_idxs, dtype=np.uint32)
            pvar = pvar.loc[variant_idxs]

        log.info(f"Reading {filename_noext}.psam")

        with open(filename_noext + ".psam") as file:
            first_line = file.readline().strip()
            psam_has_header = first_line.startswith(("#FID", "FID", "#IID", "IID"))

        psam = pd.read_csv(
            filename_noext + ".psam",
            sep=r"\s+",
            header="infer" if psam_has_header else None,
            names=(
                None
                if psam_has_header
                else ["FID", "IID", "PAT", "MAT", "SEX", "PHENO1"]
            ),
        )
        psam = psam.rename(columns={"#IID": "IID", "#FID": "FID"})
        file_num_samples = len(psam.index)

        if sample_ids is not None:
            sample_idxs = np.array(psam.index[psam["IID"].isin(list(sample_ids))])

        if sample_idxs is None:
            num_samples = file_num_samples
        else:
            num_samples = np.size(sample_idxs)
            sample_idxs = np.array(sample_idxs, dtype=np.uint32)
            psam = psam.loc[sample_idxs]

        # required arrays: variant_idxs + sample_idxs + genotypes
        if phased:
            required_ram = (
                num_samples + num_variants + num_variants * 2 * num_samples
            ) * 4
        else:
            required_ram = (num_samples + num_variants) * 4 + num_variants * num_samples
        log.info(
            f">{required_ram / 1024**3:.2f} GiB of RAM are required to process {num_samples} samples with {num_variants} variants each"
        )
        log.info(f"Reading {filename_noext}.pgen")

        pgen_reader = pg.PgenReader(
            str.encode(filename_noext + ".pgen"),
            raw_sample_ct=file_num_samples,
            variant_ct=file_num_variants,
            sample_subset=sample_idxs,
        )

        if phased:
            genotypes_: np.ndarray = np.empty(
                (num_variants, 2 * num_samples), dtype=np.int32
            )  # cannot use int8 because of pgenlib
            pgen_reader.read_alleles_list(variant_idxs, genotypes_)
            genotypes: np.ndarray = genotypes_.astype(np.int8).reshape(
                (num_variants, num_samples, 2)
            )
        else:
            genotypes = np.empty((num_variants, num_samples), dtype=np.int8)
            Parallel(n_jobs=n_jobs, backend="threading")(
                delayed(pgen_reader.read)(variant_idx, genotypes[i])
                for i, variant_idx in enumerate(tqdm(variant_idxs))
            )

        log.info("Constructing SNPObject")

        snpobj = SNPObject(
            calldata_gt=genotypes,
            samples=psam["IID"].to_numpy() if "IID" in psam else None,
            variants_ref=pvar["REF"].to_numpy() if "REF" in pvar else None,
            variants_alt=pvar["ALT"].to_numpy() if "ALT" in pvar else None,
            variants_chrom=pvar["#CHROM"].to_numpy() if "#CHROM" in pvar else None,
            variants_filter_pass=(
                pvar["FILTER"].to_numpy() if "FILTER" in pvar else None
            ),
            variants_id=pvar["ID"].to_numpy() if "ID" in pvar else None,
            variants_pos=pvar["POS"].to_numpy() if "POS" in pvar else None,
            variants_qual=pvar["QUAL"].to_numpy() if "QUAL" in pvar else None,
        )

        log.info("Finished constructing SNPObject")
        return snpobj
