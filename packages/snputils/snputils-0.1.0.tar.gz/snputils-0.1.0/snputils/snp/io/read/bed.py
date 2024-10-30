import logging
import pathlib
from typing import Optional, Tuple

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
class BEDReader(SNPBaseReader):
    def _read_bim(
        self,
        file_path_no_ext: pathlib.Path,
        variant_ids: Optional[npt.ArrayLike],
        variant_idxs: Optional[npt.ArrayLike],
    ) -> Tuple[pd.DataFrame, int, npt.ArrayLike, int]:
        """
        Reads the .bim file associated with the BED fileset.

        Args:
            file_path_no_ext: Path to the BED fileset without the extension.
            variant_ids: List of variant IDs to filter the variants. If None, all variants are read.
            variant_idxs: List of variant indices to filter the variants. If None, all variants are read.

        Returns:
            Tuple containing the filtered DataFrame, total number of variants in the file, variant indices, and the number of selected variants.
        """
        log.info(f"Reading {file_path_no_ext}.bim")

        bim = pd.read_csv(
            file_path_no_ext.with_suffix(".bim"),
            sep=r"\s+",
            # https://www.cog-genomics.org/plink/2.0/formats#bim
            names=[
                "Chromosome code",
                "Variant ID",
                "Position (cM)",
                "Base-pair coordinate",
                "ALT allele code",
                "REF allele code",
            ],
        )
        file_num_variants = len(bim.index)

        if variant_ids is not None:
            variant_idxs = bim.index[bim["Variant ID"].isin(variant_ids)].tolist()

        if variant_idxs is None:
            num_variants = file_num_variants
            variant_idxs = np.arange(num_variants, dtype=np.uint32)
        else:
            num_variants = np.size(variant_idxs)
            variant_idxs = np.array(variant_idxs, dtype=np.uint32)
            bim = bim.loc[variant_idxs]

        return bim, file_num_variants, variant_idxs, num_variants

    def _read_fam(
        self,
        file_path_no_ext: pathlib.Path,
        sample_ids: Optional[npt.ArrayLike],
        sample_idxs: Optional[npt.ArrayLike],
    ) -> Tuple[pd.DataFrame, int, npt.ArrayLike, int]:
        """
        Reads the .fam file associated with the BED fileset.

        Args:
            file_path_no_ext: Path to the BED fileset without the extension.
            sample_ids: List of sample IDs to filter the samples. If None, all samples are read.
            sample_idxs: List of sample indices to filter the samples. If None, all samples are read.

        Returns:
            Tuple containing the filtered DataFrame, total number of samples in the file, sample indices, and the number of selected samples.
        """
        log.info(f"Reading {file_path_no_ext}.fam")

        fam = pd.read_csv(
            file_path_no_ext.with_suffix(".fam"),
            sep=r"\s+",
            # https://www.cog-genomics.org/plink/2.0/formats#fam
            names=[
                "Family ID",
                "Individual ID",
                "Father ID",
                "Mother ID",
                "Sex code",
                "Phenotype value",
            ],
        )
        file_num_samples = len(fam.index)

        if sample_ids is not None:
            sample_idxs = fam.index[fam["Individual ID"].isin(sample_ids)].tolist()

        if sample_idxs is None:
            num_samples = file_num_samples
        else:
            num_samples = np.size(sample_idxs)
            sample_idxs = np.array(sample_idxs, dtype=np.uint32)
            fam = fam.loc[sample_idxs]

        return fam, file_num_samples, sample_idxs, num_samples

    def _read_bed(
        self,
        file_path_no_ext: pathlib.Path,
        sample_idxs: npt.ArrayLike,
        variant_idxs: npt.ArrayLike,
        phased: bool,
        n_jobs: int,
        file_num_variants: int,
        num_variants: int,
        file_num_samples: int,
        num_samples: int,
    ) -> npt.ArrayLike:
        """
        Reads the .bed file associated with the BED fileset.

        Args:
            file_path_no_ext: Path to the BED fileset without the extension.
            sample_idxs: Indices of the samples to be read.
            variant_idxs: Indices of the variants to be read.
            phased: Whether to read and store the genotypes as phased.
            n_jobs: Number of parallel jobs to use for reading (only applicable when phased is False).
            file_num_variants: Total number of variants in the .bim file.
            num_variants: Number of selected variants to read.
            file_num_samples: Total number of samples in the .fam file.
            num_samples: Number of selected samples to read.

        Returns:
            Numpy array containing the genotype data.
        """
        # Calculate the required RAM for processing the data
        if phased:
            required_ram = (
                num_samples + num_variants + num_variants * 2 * num_samples
            ) * 4
        else:
            required_ram = (num_samples + num_variants) * 4 + num_variants * num_samples
        log.info(
            f">{required_ram / 1024**3:.2f} GiB of RAM are required to process {num_samples} samples with {num_variants} variants each"
        )
        log.info(f"Reading {file_path_no_ext}.bed")

        # Initialize the PgenReader from pgenlib
        pgen_reader = pg.PgenReader(
            str.encode(str(file_path_no_ext.with_suffix(".bed"))),
            raw_sample_ct=file_num_samples,
            variant_ct=file_num_variants,
            sample_subset=sample_idxs,
        )

        # Read the genotype data
        if phased:
            genotypes = np.empty(
                (num_variants, 2 * num_samples), dtype=np.int32
            )  # cannot use int8 because of pgenlib
            pgen_reader.read_alleles_list(variant_idxs, genotypes)
            genotypes = genotypes.astype(np.int8).reshape(
                (num_variants, num_samples, 2)
            )
        else:
            genotypes = np.empty((num_variants, num_samples), dtype=np.int8)
            Parallel(n_jobs=n_jobs, backend="threading")(
                delayed(pgen_reader.read)(variant_idx, genotypes[i])
                for i, variant_idx in enumerate(tqdm(variant_idxs))
            )

        return genotypes

    def read(
        self,
        sample_ids: Optional[npt.ArrayLike] = None,
        sample_idxs: Optional[npt.ArrayLike] = None,
        variant_ids: Optional[npt.ArrayLike] = None,
        variant_idxs: Optional[npt.ArrayLike] = None,
        phased: bool = True,
        n_jobs: int = 1,
    ) -> SNPObject:
        """
        Read a bed fileset (bed, bim, fam) into a SNPObject.

        Args:
            sample_ids: List of sample IDs to read. If None, all samples are read.
            sample_idxs: List of sample indices to read. If None, all samples are read.
            variant_ids: List of variant IDs to read. If None, all variants are read.
            variant_idxs: List of variant indices to read. If None, all variants are read.
            phased: Whether to read and store the genotypes as phased.
                Note that due to the pgenlib backend, when phased is True, 8 times as much RAM is required.
                Nonetheless, the calldata_gt will only be double the size.
                WARNING: bed files do not store phase information. If you need it, use vcf or pgen.
            n_jobs: Number of jobs to use for parallel reading. -1 means all CPUs.
                Not used if phased is False, since parallel reading is not supported.

        Returns:
            SNPObject:
                SNPObject containing the data from the bed fileset.
                If phased is True, calldata_gt is stored as a numpy array of shape (num_variants, num_samples, 2) and dtype int8 containing 0, 1.
                If phased is False, calldata_gt is stored as a numpy array of shape (num_variants, num_samples) and dtype int8 containing 0, 1, 2.
        """
        assert (
            sample_idxs is None or sample_ids is None
        ), "Only one of sample_idxs and sample_ids can be specified"
        assert (
            variant_idxs is None or variant_ids is None
        ), "Only one of variant_idxs and variant_ids can be specified"

        file_path_no_ext = self.filename
        if file_path_no_ext.suffix == ".bed":
            file_path_no_ext = file_path_no_ext.with_suffix("")

        bim, file_num_variants, variant_idxs, num_variants = self._read_bim(
            file_path_no_ext, variant_ids, variant_idxs
        )

        fam, file_num_samples, sample_idxs, num_samples = self._read_fam(
            file_path_no_ext, sample_ids, sample_idxs
        )

        genotypes = self._read_bed(
            file_path_no_ext,
            sample_idxs,
            variant_idxs,
            phased,
            n_jobs,
            file_num_variants,
            num_variants,
            file_num_samples,
            num_samples,
        )

        log.info("Constructing SNPObject")

        snpobj = SNPObject(
            calldata_gt=genotypes,
            samples=fam["Individual ID"].to_numpy(),
            variants_ref=bim["REF allele code"].to_numpy(),
            variants_alt=bim["ALT allele code"].to_numpy(),
            variants_chrom=bim["Chromosome code"].to_numpy(),
            # variants_filter_pass=None,
            variants_id=bim["Variant ID"].to_numpy(),
            variants_pos=bim["Base-pair coordinate"].to_numpy(),
            # variants_qual=None
        )

        log.info("Finished constructing SNPObject")
        return snpobj
