import logging
import warnings
import numpy as np
import pandas as pd
import sys

log = logging.getLogger(__name__)

#sys.path.insert(1, 'snputils/genobj/ancestry/local')
from snputils.ancestry.genobj.local import LocalAncestryObject
from .base import LAIBaseReader

@LAIBaseReader.register
class MSPReader(LAIBaseReader):
    def read(self):
        log.info(f"Reading msp file: {self.filename}")
        
        with open(self.filename) as f:
            first_line = f.readline()
            second_line = f.readline()
        
        first_line_ = [h.replace('\n', '') for h in first_line.split("\t")]
        second_line_ = [h.replace('\n', '') for h in second_line.split("\t")]
        if "#chm" in first_line_:
            comment = None
            header = first_line_
        elif "#chm" in second_line_:
            comment = first_line
            header = second_line_
        # We leave #chm as the reference value for the header
        else:
            raise ValueError(f".msp header not found, first line:\n{first_line}\nsecond line:\n{second_line}")

        # Make sure there are no repeated columns
        assert len(header) == len(set(header)), "Repeated columns"

        # We are assuming that the names of the variables are standard; otherwise it 
        # should be adapted to be able to receive the column names from the user
        msp_df = pd.read_csv(self.filename, sep="\t", comment="#", names=header)

        chromosome = msp_df['#chm'].to_numpy()
        column_counter = 1
        try:
            physical_pos = msp_df[['spos','epos']].to_numpy()
            column_counter+=2
        except:
            physical_pos = None
            print("Physical Position data not found")
        try:
            centimorgan_pos = msp_df[['sgpos','egpos']].to_numpy()
            column_counter+=2
        except:
            centimorgan_pos = None
            print("Genetic (centimorgan) Position data not found")
        try:
            window_size = msp_df['n snps'].to_numpy()
            column_counter+=1
        except:
            window_size = None
            print("Window Size data not found")
        lai_array = msp_df[msp_df.columns[column_counter:]].to_numpy()        
        
        haplotype_IDs = msp_df.columns[column_counter:].to_list()
        sample_IDs = self.get_samples(msp_df, column_counter)
        n_samples = len(sample_IDs)
        assert n_samples == int(lai_array.shape[1] / 2), "Something wrong in n_samples"
        n_classes = len(np.unique(lai_array))
        
        ancestry_map = None
        if comment is not None:
            ancestry_map = self.get_ancestry_map_from_comment(comment)
            if len(ancestry_map) != n_classes:
                warnings.warn("Number of classes and number of ancestries in "
                              "ancestry map do not match.")
        else:
            warnings.warn("Ancestry Map was not provided. Assumming AFR:0, AHG:1, "
                          "EAS:2, EUR:3, NAT:4, OCE:5, SAS:6, WAS:7.")
            ancestry_map = {
                "AFR":0, "AHG":1, 
                "EAS":2, "EUR":3, 
                "NAT":4, "OCE":5, 
                "SAS":6, "WAS":7
            }
            if len(ancestry_map) != n_classes:
                warnings.warn("Number of classes and number of ancestries in "
                              "ancestry map do not match. It is recommended to "
                              "provide an .msp file that contains the ancestry "
                              "map as a comment in the first line.")

        laiobj = LocalAncestryObject(haplotype_IDs = haplotype_IDs,
                                     lai_array=lai_array, 
                                     n_samples=n_samples,
                                     sample_IDs=sample_IDs,
                                     ancestry_map=ancestry_map,
                                     window_size=window_size,
                                     n_classes=n_classes,
                                     centimorgan_pos=centimorgan_pos,
                                     chromosome=chromosome,
                                     physical_pos=physical_pos)
        log.info(f"Finished reading msp file: {self.filename}")
        return laiobj

    def get_samples(self, msp_df, first_lai_col_indx):
        """
        Function for getting sample IDs from a pandas DF containing the output data
        From: https://github.com/AI-sandbox/gnomix/blob/main/src/postprocess.py

        Args:
            msp_df: pandas DataFrame containing the data
            first_lai_col_indx: index of the first column containing LAI data

        Returns:
            list: list of sample IDs
        """
        # get all columns including sample names
        query_samples_dub = msp_df.columns[first_lai_col_indx:]

        # only keep 1 of maternal/paternal
        single_ind_idx = np.arange(0 ,len(query_samples_dub) ,2)
        query_samples_sing = query_samples_dub[single_ind_idx]

        # remove the suffix
        query_samples = [qs[:-2] for qs in query_samples_sing]

        return query_samples

        #TODO: sanity check that if comment, all clusters appear in the data. (almenys avisar amb un warning)

    def get_ancestry_map_from_comment(self, comment):
        # Revise if valid for all msp comments.

        comment = comment.split(' ')[-1].replace('\n','').split('\t')
        ancestry_map = {}
        for elem in comment:
            name, num = elem.split('=')
            ancestry_map[num] = name
        
        return ancestry_map


    def _sanity_check(self) -> None:
        # Some sanity check is currently done in self.read()
        return

