import logging
from typing import List, Optional

import allel
import numpy as np

from snputils.snp.genobj.snpobj import SNPObject
from snputils.snp.io.read.base import SNPBaseReader

log = logging.getLogger(__name__)


@SNPBaseReader.register
class VCFReader(SNPBaseReader):
    def read(
        self,
        fields: Optional[List[str]] = None,
        exclude_fields: Optional[List[str]] = None,
        rename_fields: Optional[dict] = None,
        fills: Optional[dict] = None,
        region: Optional[str] = None,
        samples: Optional[List[str]] = None,
        phased: bool = True,
    ) -> SNPObject:
        """
        Read a vcf file into a SNPObject.

        Args:
            fields: Fields to extract data for. e.g., ['variants/CHROM', 'variants/POS',
                'calldata/GT']. If you are feeling lazy, you can drop the 'variants/'
                and 'calldata/' prefixes, in which case the fields will be matched
                against fields declared in the VCF header, with variants taking priority
                over calldata if a field with the same ID exists both in INFO and FORMAT
                headers. I.e., ['CHROM', 'POS', 'DP', 'GT'] will work, although watch out
                for fields like 'DP' which can be both INFO and FORMAT. To extract all
                fields, provide just the string '*'. To extract all variants fields
                (including all INFO fields) provide 'variants/*'. To extract all
                calldata fields (i.e., defined in FORMAT headers) provide 'calldata/*'.
            exclude_fields: Fields to exclude. E.g., for use in combination with fields='*'.
            rename_fields: Fields to be renamed. Should be a dictionary mapping old to new names.
            fills: Override the fill value used for empty values. Should be a dictionary
                mapping field names to fill values.
            region: Genomic region to extract variants for. If provided, should be a
                tabix-style region string, which can be either just a chromosome name
                (e.g., '2L'), or a chromosome name followed by 1-based beginning and
                end coordinates (e.g., '2L:100000-200000'). Note that only variants
                whose start position (POS) is within the requested range will be included.
                This is slightly different from the default tabix behaviour, where a
                variant (e.g., deletion) may be included if its position (POS) occurs
                before the requested region but its reference allele overlaps the
                region - such a variant will not be included in the data returned
                by this function.
            samples: Selection of samples to extract calldata for. If provided, should be
                a list of strings giving sample identifiers. May also be a list of
                integers giving indices of selected samples.
            phased: Whether to store the genotypes as phased.

        Returns:
            snpobj: SNPObject containing the data from the vcf file.
                If phased is True, calldata_gt is stored as a numpy array of shape
                (num_variants, num_samples, 2) and dtype int8 containing 0, 1.
                If phased is False, calldata_gt is stored as a numpy array of shape
                (num_variants, num_samples) and dtype int8 containing 0, 1, 2.
        """
        log.info(f"Reading {self.filename}")

        vcf_dict = allel.read_vcf(
            str(self.filename),
            fields=fields,
            exclude_fields=exclude_fields,
            rename_fields=rename_fields,
            fills=fills,
            region=region,
            samples=samples,
        )
        assert vcf_dict is not None  # suppress Flake8 warning

        genotypes = vcf_dict["calldata/GT"].astype(np.int8)
        if not phased:
            genotypes = genotypes.sum(axis=2, dtype=np.int8)

        snpobj = SNPObject(
            calldata_gt=genotypes,
            samples=vcf_dict["samples"],
            variants_ref=vcf_dict["variants/REF"],
            variants_alt=vcf_dict["variants/ALT"],
            variants_chrom=vcf_dict["variants/CHROM"],
            variants_filter_pass=vcf_dict["variants/FILTER_PASS"],
            variants_id=vcf_dict["variants/ID"],
            variants_pos=vcf_dict["variants/POS"],
            variants_qual=vcf_dict["variants/QUAL"],
        )

        log.info(f"Finished reading {self.filename}")
        return snpobj
