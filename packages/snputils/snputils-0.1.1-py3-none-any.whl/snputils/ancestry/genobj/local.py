import numpy as np
import copy
from typing import Union, List, Dict, Optional
from .base import AncestryObject

class LocalAncestryObject(AncestryObject):
    """
    Abstract class for local ancestry inference
    """
    def __init__(self,
                 haplotype_IDs: List,
                 lai_array: np.ndarray,
                 n_samples: Optional[int] = None,
                 sample_IDs: Optional[List] = None,
                 ancestry_map: Optional[Dict] = None,
                 window_size: Optional[np.ndarray] = None,
                 n_classes: Optional[int] = None,
                 centimorgan_pos: Optional[np.ndarray] = None,
                 chromosome: Optional[np.ndarray] = None,
                 physical_pos: Optional[np.ndarray] = None) -> None:

        assert len(lai_array.shape) == 2
        if n_classes is None:
            n_classes = len(np.unique(lai_array))

        super(LocalAncestryObject, self).__init__(n_samples, n_classes)

        self.__haplotype_IDs = haplotype_IDs
        self.__lai = lai_array
        self.__window_size = window_size
        self.__centimorgan_pos = centimorgan_pos
        self.__sample_IDs = sample_IDs
        self.__chromosome = chromosome
        self.__physical_pos = physical_pos
        self.__ancestry_map = ancestry_map

    def copy(self):
        """
        Create and return a copy of the LocalAncestryObject.
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
    def haplotype_IDs(self) -> list:
        """
        Retrieve all haplotype IDs

        Returns:
            np.ndarray: array containing the haplotype IDs.
        """
        return self.__haplotype_IDs
    
    @haplotype_IDs.setter
    def haplotype_IDs(self, x):
        """
        Update haplotype_IDs.
        """
        self.__haplotype_IDs = x
    
    @property
    def lai(self) -> np.ndarray:
        """
        Retrieve LAI array

        Returns:
            np.ndarray: array containing the population indexes.
        """
        return self.__lai
        
    @lai.setter
    def lai(self, x):
        """
        Update lai.
        """
        self.__lai = x

    @property
    def window_size(self) -> Optional[np.ndarray]:
        """
        Retrieve window size

        Returns:
            np.ndarray: array containing the window sizes.
        """
        return self.__window_size
        
    @window_size.setter
    def window_size(self, x):
        """
        Update window_size.
        """
        self.__window_size = x

    @property
    def centimorgan_pos(self) -> Optional[np.ndarray]:
        """
        Retrieve centimorgan_pos

        Returns:
            np.ndarray: array containing the start and end centimorgan positions.
        """
        return self.__centimorgan_pos
        
    @centimorgan_pos.setter
    def centimorgan_pos(self, x):
        """
        Update centimorgan_pos.
        """
        self.__centimorgan_pos = x

    @property
    def physical_pos(self) -> Optional[np.ndarray]:
        """
        Retrieve physical_pos

        Returns:
            np.ndarray: array containing the start and end of physical positions.
        """
        return self.__physical_pos
        
    @physical_pos.setter
    def physical_pos(self, x):
        """
        Update physical_pos.
        """
        self.__physical_pos = x

    @property
    def sample_IDs(self) -> Optional[List]:
        """
        Retrieve sample_IDs

        Returns:
            np.ndarray: list containing the sample IDs.
        """
        return self.__sample_IDs
    
    @property
    def ancestry_map(self) -> dict:
        """
        Map indexes in the lai array and ancestry codes

        Returns:
            dict: Ancestry codes dictionary
        """
        return self.__ancestry_map
        
    @sample_IDs.setter
    def sample_IDs(self, x):
        """
        Update sample_IDs.
        """
        self.__sample_IDs = x

    @property
    def chromosome(self) -> Optional[np.ndarray]:
        """
        Retrieve chromosome

        Returns:
            np.ndarray: array containing the chromosome numbers.
        """
        return self.__chromosome
        
    @chromosome.setter
    def chromosome(self, x):
        """
        Update chromosome.
        """
        self.__chromosome = x
    
    def n_samples(self) -> int:
        """
        Retrieves the number of samples based on the sample IDs.

        Returns:
            int: The number of samples.
        """
        if self.__sample_IDs is not None:
            return len(self.__sample_IDs)
        elif self.__haplotype_IDs is not None:
            # Divide by 2 because each sample has two haplotypes (e.g., .0 and .1)
            return len(self.__haplotype_IDs) // 2
        else:
            raise ValueError("Sample IDs or haplotype IDs not found.")

    def drop_window(self, list_of_windows_index):
        """
        Modify the LAI object by deleting all the data corresponding to the 
        windows listed, by index, in list_of_windows_index.

        Returns:
            
        """
        # DO NOT CHANGE: ancestry_map, n_classes, n_samples, sample_IDs, haplotype_IDs
        # CHANGE: lai_array, chromosome, centimorgan_pos, physical_pos, window_size
        self.__chromosome = np.delete(self.__chromosome, list_of_windows_index)
        self.__lai = np.delete(self.__lai, list_of_windows_index, axis=0)
        try:
            self.__centimorgan_pos = np.delete(self.__centimorgan_pos, list_of_windows_index, axis=0)
        except:
            pass
        self.__physical_pos = np.delete(self.__physical_pos, list_of_windows_index, axis=0)
        try:
            self.__window_size = np.delete(self.__window_size, list_of_windows_index)
        except:
            pass

        return

    def filter_samples(
        self,
        samples: Union[str, List[str], np.ndarray, None] = None,
        indexes: Union[int, List[int], np.ndarray, None] = None,
        include: bool = True,
        inplace: bool = False
    ) -> Optional['LocalAncestryObject']:
        """
        Filter samples according to 'samples' names, or based on sample 'indexes'.
        It can either include or exclude samples that match the specified criteria.

        Args:
            samples : Union[str, List[str], np.ndarray, None]), default=None
                 Samples to filter data by.
            indexes : Union[int, List[int], np.ndarray, None]), default=None
                Indexes of samples to include or exclude.
            include : bool, default=True
                If True, includes samples that match the specified criteria,
                otherwise excludes them.
            inplace : bool, default=False
                A boolean flag that controls the behavior of the method.
                If True, the operation is done in-place and the original object is modified,
                otherwise, a new object is created and returned.

        Returns:
            Optional[LocalAncestryObject]: Returns the modified object if inplace=False,
            otherwise modifies the original object in place and returns None.

        Raises:
            ValueError: If both samples and indexes are provided.
            UserWarning: If neither samples nor indexes are provided.
        """
        # Change input format to list
        if isinstance(samples, (str, int)):
            samples = [samples]
        elif isinstance(samples, np.ndarray):
            samples = samples.tolist()

        if isinstance(indexes, int):
            indexes = [indexes]
        elif isinstance(indexes, np.ndarray):
            indexes = indexes.tolist()

        if indexes is not None:
            if samples:
                raise ValueError("Indexes should not be provided when samples are specified.")
            else:
                # Vectorized conversion of sample indexes to haplotype indexes
                haplotype_indexes = np.repeat(indexes, 2) * 2 + np.tile([0, 1], len(indexes))
                indexes = np.zeros(self.n_samples() * 2, dtype=np.bool_)
                indexes[haplotype_indexes] = True
        elif samples:
            # Vectorized sample name matching with haplotype IDs
            haplotype_ids = np.array(self['haplotype_IDs'])
            sample_names = np.array([hap.split('.')[0] for hap in haplotype_ids])
            indexes = np.in1d(sample_names, samples)
        else:
            raise UserWarning("At least one of samples or indexes should be provided.")

        if not include:
            # Invert boolean array from True to False and vice-versa
            indexes = ~indexes

        # Perform filtering in-place or return a new object
        filtered_sample_ids = np.array(self['sample_IDs'])[indexes[::2]]
        filtered_haplotype_ids = np.array(self['haplotype_IDs'])[indexes]
        filtered_lai = np.array(self['lai'])[:, indexes]

        if inplace:
            self['sample_IDs'] = filtered_sample_ids.tolist()
            self['haplotype_IDs'] = filtered_haplotype_ids.tolist()
            self['lai'] = filtered_lai
            return None
        else:
            laiobj = self.copy()
            laiobj['sample_IDs'] = filtered_sample_ids.tolist()
            laiobj['haplotype_IDs'] = filtered_haplotype_ids.tolist()
            laiobj['lai'] = filtered_lai
            return laiobj
    
    def _sanity_check(self) -> None:

        # Make sure the number of classes makes sense
        assert len(np.unique(self.__lai) == self.n_ancestries)

        # In the case of having windows, the centimorgan positions will be the 
        # beginning and end of the window as in msp files.
        if self.__centimorgan_pos is not None:
            if self.__window_size == 1:
                assert len(self.__centimorgan_pos.shape) == 1
            else:
                assert len(self.__centimorgan_pos.shape) == 2

        return
