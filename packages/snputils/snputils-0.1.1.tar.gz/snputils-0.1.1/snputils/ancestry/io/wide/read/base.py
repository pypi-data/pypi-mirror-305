import abc
from pathlib import Path
from typing import Optional, Union

import numpy as np


# TODO: use pathlib objects as arguments instead of plain strings for file paths
class BaseWideReader(abc.ABC):
    """Abstract class for global ancestry readers
    """
    def __init__(self, Q_file: Union[str, Path], P_file: Union[str, Path], sample_id_file: Optional[Union[str, Path]]=None,
                 snp_file: Optional[Union[str, Path]]=None, ancestry_file: Optional[Union[str, Path]]=None) -> None:
        self.__Q_file = Path(Q_file)
        self.__P_file = Path(P_file)
        self.__sample_id_file = Path(sample_id_file) if sample_id_file is not None else None
        self.__snp_file = Path(snp_file) if snp_file is not None else None
        self.__ancestry_file = Path(ancestry_file) if ancestry_file is not None else None


    @abc.abstractmethod
    def read(self) -> None: # pragma: no cover
        pass

    def _read_sample_ids(self) -> Optional[np.ndarray]:
        if self.sample_id_file is None:
            return None
        if self.sample_id_file.suffix == ".txt":
            return np.genfromtxt(self.sample_id_file, dtype=str)
        elif self.sample_id_file.suffix == ".fam":
            return np.genfromtxt(self.sample_id_file, dtype=str, usecols=1)
        else:
            raise ValueError("Invalid file format for sample IDs. Should be a single-column txt file or a .fam file.")
    
    def _read_snps(self) -> Optional[np.ndarray]:
        if self.snp_file is None:
            return None
        if self.snp_file.suffix == ".txt":
            return np.genfromtxt(self.snp_file, dtype=str)
        elif self.snp_file.suffix == ".bim":
            return np.genfromtxt(self.snp_file, dtype=str, usecols=1)
        else:
            raise ValueError("Invalid file format for SNP IDs. Should be a single-column txt file or a .bim file.")

    def _read_ancestries(self) -> Optional[np.ndarray]:
        if self.ancestry_file is None:
            return None
        if self.ancestry_file.suffix == ".map":
            return np.genfromtxt(self.ancestry_file, dtype=str)
        else:
            raise ValueError("Invalid file format for ancestry labels. Should be a single-column txt file.")

    @property
    def Q_file(self) -> str:
        """Retrieve path to file storing LAI info

        Returns:
            str: path to file storing LAI info
        """
        return self.__Q_file
    
    @property
    def P_file(self) -> str:
        """Retrieve path to file storing P/F matrix

        Returns:
            str: path to file storing P/F matrix
        """
        return self.__P_file
    
    @property
    def sample_id_file(self) -> Optional[str]:
        """Retrieve path to single-column text file storing sample IDs in order

        Returns:
            str: path to file storing sample IDs
        """
        return self.__sample_id_file
    
    @property
    def snp_file(self) -> Optional[str]:
        """Retrieve path to single-column text file storing SNP ID in order

        Returns:
            str: path to file storing SNP info
        """
        return self.__snp_file
    
    @property
    def ancestry_file(self) -> Optional[str]:
        """Retrieve path to single-column text file storing ancestry label in order

        Returns:
            str: path to file storing ancestry label
        """
        return self.__ancestry_file
