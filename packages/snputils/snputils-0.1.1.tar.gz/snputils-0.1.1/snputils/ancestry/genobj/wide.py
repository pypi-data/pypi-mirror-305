from typing import Dict, Iterable, Optional, Union

import numpy as np

from .base import AncestryObject


class WideAncestryObject(AncestryObject):
    """
    Abstract class for wide (global) ancestry inference
    """
    def __init__(self,
                 Q: np.ndarray,
                 P: np.ndarray,
                 sample_IDs: Optional[Iterable] = None,
                 ancestries: Optional[Iterable] = None,
                 snps: Optional[Iterable] = None,
                 n_snps: Optional[int] = None,
                 ) -> None:

        n_samples = Q.shape[0]
        n_snps = P.shape[0]
        n_ancestries = Q.shape[1]

        if sample_IDs is None:
            sample_IDs = tuple(range(n_samples))

        if snps is None:
            snps = tuple(range(n_snps))

        super(WideAncestryObject, self).__init__(n_samples, n_ancestries)

        self.__Q = Q
        self.__P = P
        self.__sample_IDs = np.asarray(sample_IDs)
        self.__snps = np.asarray(snps)
        self.__ancestries = np.asarray(ancestries)
        self.__n_samples = n_samples
        self.__n_ancestries = n_ancestries
        self.__n_snps = n_snps

        self._sanity_check()


    def copy(self):
        """
        Create and return a copy of the WideAncestryObject.
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
    
    def keys(self):
        """
        Return the list of attribute names.
        """
        return [attr.replace('_LocalAncestryObject__', '').replace(
            '_AncestryObject__', '') for attr in vars(self)]

    @property
    def Q(self) -> np.ndarray:
        """
        Retrieve Q matrix containing per-sample ancestry assignments.

        Returns:
            np.ndarray: Q matrix
        """
        return self.__Q
    
    @property
    def P(self) -> np.ndarray:
        """
        Return P matrix containing per-population SNP frequency.

        Returns:
            np.ndarray: P matrix
        """
        return self.__P
    
    @property
    def F(self) -> np.ndarray:
        """
        Alias for WideAncestryObject.P

        Returns:
            np.ndarray: P matrix
        """
        return self.P

    @property
    def snps(self) -> np.ndarray:
        """
        Retrieve SNPs

        Returns:
            tuple: tuple containing the SNP identifiers.
        """
        return self.__snps
    
    @property
    def n_snps(self) -> int:
        """
        Retrieve number of SNPs

        Returns:
            int: number of SNPs
        """
        return len(self.__snps)
    
    @property
    def n_samples(self) -> int:
        """
        Retrieve number of samples

        Returns:
            int: number of samples
        """
        return len(self.__sample_IDs)
    
    @property
    def n_ancestries(self) -> int:
        """
        Retrieve number of ancestries

        Returns:
            int: number of ancestries
        """
        return self.__n_ancestries
        
    @snps.setter
    def snps(self, x: Iterable):
        """
        Update snps from a given iterable.
        """
        num_x = len(x)
        assert num_x == self.n_snps, f'Number of given SNPs does not match current number of SNPs (found {num_x}, expected {self.n_snps}). Aborting update.'
        self.__snps = np.asarray(x)
    
    @property
    def sample_IDs(self) -> np.ndarray:
        """
        Retrieve sample_IDs.

        Returns:
            np.ndarray: list containing the sample IDs.
        """
        return self.__sample_IDs
        
    @sample_IDs.setter
    def sample_IDs(self, x: Iterable):
        """
        Update sample_IDs from a given iterable.
        """
        num_x = len(x)
        assert num_x == self.n_samples, f'Number of samples does not match sample IDs (found {num_x}, expected {self.n_samples}). Aborting update.'
        self.__sample_IDs = np.asarray(x)
    
    @property
    def ancestries(self) -> Union[tuple, None]:
        """
        Retrieve sample-wise ancestry labels.

        Returns:
            tuple: tuple containing the ancestry labels. If no ancestries labels are present, return None.
        """
        return self.__ancestries
    
    @ancestries.setter
    def ancestries(self, x: Iterable):
        """
        Update sample-wise labels from a given iterable.
        """
        unique_x = np.unique(x)
        num_unique_x = len(unique_x)
        num_x = len(x)
        assert num_unique_x <= self.n_ancestries, f'Number of unique ancestry labels does not match given ancestry labels (found {num_unique_x}, expected {self.n_ancestries} or less). Aborting update.'
        assert num_x == self.n_samples, f'Number of given labels does not match number of samples (found {num_x}, expected {self.n_samples}). Aborting update.'
        self.__ancestries = np.asarray(x)


    def _sanity_check(self) -> None:
        assert self.Q.shape[0] == self.n_samples, 'Q matrix does not match number of samples'
        assert self.P.shape[1] == self.n_ancestries, 'P matrix does not match number of ancestries'
        assert self.Q.shape[1] == self.n_ancestries, 'Q matrix does not match number of ancestries'
        if self.snps is not None:
            assert self.P.shape[0] == len(self.snps), 'P matrix does not match number of SNPs'

        if self.sample_IDs is not None:
            assert len(self.sample_IDs) == self.n_samples, 'Number of samples does not match sample IDs'
        return
