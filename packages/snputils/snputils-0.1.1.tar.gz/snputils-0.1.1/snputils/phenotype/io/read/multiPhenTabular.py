import logging
import pandas as pd
import os
import sys
from typing import List, Optional

log = logging.getLogger(__name__)

from snputils.phenotype.genobj import MultiPhenotypeObject

class MultiPhenTabularReader():
    """
    Read phenotype data from a tabular file into a MultiPhenotypeObject.
    Accepted file formats = ['.xlsx', '.csv', '.map', '.smap', '.phen'].
    """ 

    def __init__(self, filename):
        self._filename = filename
    
    def read(self, samples_idx: int=0, phen_names: Optional[List[str]] = None, sep: str=',', header: int=0, drop: bool=False):
        """
        Args:
            samples_idx: Index of the column containing sample IDs. By default, the first 
                column is assumed to contain sample IDs.
            phen_names: List of phenotype column names. If provided, all columns with 
                phenotypes will be renamed.
            sep:
                The separator used in '.csv', '.tsv', or '.map' file.
            header: Specify the row number(s) that contain column labels and indicate 
                the start of the data, using zero-based indexing. By default, column 
                names are inferred from the first line of the file (equivalent to 
                header=0) if no names are provided explicitly. If you pass column 
                names explicitly using the names parameter, the behavior is similar 
                to header=None. To replace existing column names, explicitly use 
                header=0.
            drop: If True, remove columns that are not specified in ``phen_names`` 
                and are different from the ``samples`` column.

        Returns:
            MultiPhenotypeObject: Tabular object with a ``samples`` column with sample IDs and one or 
                multiple columns with phenotype information (e.g., heihght, ancestry).
        """
        # Obtain file extension
        file_extension = os.path.splitext(self.filename)[1]
        log.info(f"Reading {file_extension} file: {self.filename}")
        
        if file_extension == '.xlsx': 
            phen_df = pd.read_excel(self.filename, header=0, index_col=None)
        
        elif file_extension == '.csv':
            phen_df = pd.read_csv(self.filename, sep=sep, header=header)
        
        elif file_extension in ['.map', '.smap']:
            phen_df = pd.read_csv(self.filename, sep=sep, header=header)
        
        elif file_extension == '.tsv':
            phen_df = pd.read_csv(self.filename, sep='\t')
            
        elif file_extension == '.phen':
            with open(self.filename, 'r') as f:
                # Read all lines of file, including the header
                contents = f.readlines()
            # Remove first line (the header line) of the .phen file
            contents = contents[1:]
            # Loop through lines and convert into a dictionary
            phen_dict = {line.split()[0]:line.split()[1].split('\n')[0] for line in contents}
            # Convert to dataframe
            phen_df = pd.DataFrame({
                'samples' : phen_dict.keys(), 
                'phenotype' : phen_dict.values()}
            )
        
        else:
            raise ValueError(f'{file_extension} not supported. Support file extensions: '
                             '[".xlsx", ".csv", ".tsv", ".map", ".smap", ".phen"]')
        
        # Rename column with sample IDs to 'samples'
        phen_df.rename(columns={phen_df.columns[samples_idx]: 'samples'}, inplace=True)

        if samples_idx != 0:
            # Reorder columns such that the 'samples' column is the first
            cols = ['samples'] + [col for col in phen_df.columns if col != 'samples']
            phen_df = phen_df[cols]
        
        if phen_names is not None:
            if drop:
                # Drop columns not provided in ``phen_names``
                non_phen_columns = list(set(phen_df.columns) - set(['samples']+phen_names))
                phen_df = phen_df.drop(non_phen_columns, axis=1)
            
            # Rename phenotype columns
            if phen_df.shape[1]-1 == len(phen_names):
                phen_df.columns.values[1:] = phen_names
            else:
                raise ValueError('Length of phen_names does not match number of phenotypes '
                                 f'in dataframe {phen_df.shape[1]-1} != {len(phen_names)}).')
        
        # Define MultiPhenotypeObject
        phenobj = MultiPhenotypeObject(phen_df=phen_df)
        
        log.info(f"Finished {file_extension} file: {self.filename}")
        
        return phenobj
    
    @property
    def filename(self) -> str:
        """Retrieve path to file storing Phenotype info
        Returns:
            str: path to file storing Phenotype info
        """
        return self._filename
