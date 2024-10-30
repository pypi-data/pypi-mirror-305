import logging
import sys
import pandas as pd

log = logging.getLogger(__name__)

from snputils.phenotype.genobj import UKBPhenotypeObject
from .base import PhenotypeBaseReader

@PhenotypeBaseReader.register
class UKBPhenReader(PhenotypeBaseReader):
    """
    Accepted file formats = ['.phe'].
    """ 
    def read(self):
        log.info(f"Reading .phe file: {self.filename}")
        
        # Read phenotype file
        phen_df = pd.read_csv(
            self.filename,
            header=None,
            delim_whitespace=True,
            names=["FID", "IID", "status"],
            dtype={"FID": str, "IID": str, "status": int},
        )
        
        cases_IDs = list(phen_df[phen_df["status"] == 2]["FID"])
        n_cases = len(cases_IDs)
        if n_cases == 0:
            raise ValueError("No case data available!")
        controls_IDs = list(phen_df[phen_df["status"] == 1]["FID"])
        n_controls = len(controls_IDs)
        if n_controls == 0:
            raise ValueError("No control data available!")
        
        sample_IDs = list(phen_df["FID"])
        n_samples = len(sample_IDs)
        assert n_samples == (n_cases+n_controls), "Something is wrong with samples"
        
        
        # "Taking care" of maternal and paternal strands
        cases_haplotypes = [case + ".0" for case in cases_IDs] + [case + ".1" for case in cases_IDs]
        controls_haplotypes = [control + ".0" for control in controls_IDs] + [control + ".1" for control in controls_IDs]
        all_haplotypes = [sample + ".0" for sample in sample_IDs] + [sample + ".1" for sample in sample_IDs]
        
        
        # Obtain phenotype object
        phenobj = UKBPhenotypeObject(sample_IDs = sample_IDs,
                                  n_samples = n_samples,
                                  cases_IDs = cases_IDs,
                                  n_cases = n_cases,
                                  controls_IDs = controls_IDs,
                                  n_controls = n_controls,
                                  all_haplotypes = all_haplotypes,
                                  cases_haplotypes = cases_haplotypes,
                                  controls_haplotypes = controls_haplotypes
                                 )
        
        log.info(f"Finished reading .phe file: {self.filename}")
        return phenobj