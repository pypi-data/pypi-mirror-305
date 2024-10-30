import numpy as np
import copy
from pandas import DataFrame

class MultiPhenotypeObject():
    """
    Class for Phenotype exploitation
    """
    def __init__(self,
                 phen_df: DataFrame) -> None:

        self.__phen_df = phen_df
        
    def copy(self):
        """
        Create and return a copy of the phenobject.
        """
        return copy.copy(self)

    def __getitem__(self, key):
        """
        To access an attribute of the class using the square bracket notation,
        similar to a dictionary.
        """
        try:
            return getattr(self, key)
        except:
            raise KeyError(f'Invalid key: {key}')

    def __setitem__(self, key, value):
        """
        To set an attribute of the class using the square bracket notation,
        similar to a dictionary.
        """
        try:
            setattr(self, key, value)
        except:
            raise KeyError(f'Invalid key: {key}')

    @property
    def phen_df(self) -> DataFrame:
        """
        Retrieve a dataframe of phenotypes with a variable number 
        of traits and a first column containing sample IDs

        Returns:
            pd.DataFrame: dataframe of phenotypes with a variable number 
                          of traits and a first column containing sample 
                          IDs
        """
        return self.__phen_df
    
    @phen_df.setter
    def phen_df(self, x):
        """
        Update phen_df.
        """
        self.__phen_df = x
    
    def n_samples(self) -> int:
        """
        Retrieve number of samples.

        Returns
        -------
        int: number of samples.
        """
        return len(self.phen_df)
    
    def filter_samples(self, samples=None, indexes=None, include=True, inplace=False):
        """
        Filter samples according to sample names, or based on sample indexes.
        It can either include or exclude samples that match the specified
        criteria.

        Parameters
        ----------
        samples : str or list
            Samples to filter data by.
        indexes : int or list
            Indexes of samples to include or exclude.
        include : bool
            If True, includes samples that match the specified criteria,
            otherwise excludes them.
        inplace : bool, default=False
            A boolean flag that controls the behavior of the method. If True,
            the operation is done in-place and the original object is modified,
            otherwise, a new object is created and returned.

        Returns
        -------
        MultiPhenotypeObject or None
            If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.
        """
        # Change input format to list
        if isinstance(samples, (str, int)) or isinstance(samples, (np.ndarray)):
            samples = [samples]
        if isinstance(indexes, (int)) or isinstance(indexes, (np.ndarray)):
            indexes = [indexes]

        if indexes:
            if samples:
                raise ValueError("Indexes should not be provided when samples "
                                 "are specified.")
            else:
                # Create vector of booleans with as many positions as samples
                # The provided indexes are set to True
                arr = np.zeros(self.n_samples(), dtype=bool)
                arr[indexes] = True
                indexes = arr

        elif samples:
            indexes = np.in1d(self.phen_df['samples'], samples)
        elif not indexes:
            warnings.warn("At least one of samples or indexes should be provided.")

        if not include:
            # Invert boolean array from True to False and vice-versa
            indexes = np.invert(indexes)

        if inplace:
            self.phen_df = self.phen_df.iloc[indexes].reset_index(drop=True)
            return None
        else:
            phenobj = self.copy()
            phenobj.phen_df = phenobj.phen_df.iloc[indexes].reset_index(drop=True)
            return phenobj