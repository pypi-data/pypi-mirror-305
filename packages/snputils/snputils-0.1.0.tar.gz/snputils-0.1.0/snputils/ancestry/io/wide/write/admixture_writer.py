import abc
from pathlib import Path
from typing import Union

import numpy as np

from snputils.ancestry.genobj.wide import WideAncestryObject
from .base import BaseWideWriter


@BaseWideWriter.register
class AdmixtureWriter(BaseWideWriter):
    """
    ADMIXTURE format wide ancestry writer
    """ 

    def __init__(self, wideobj: WideAncestryObject, filename_suffix: Union[str, Path]):
        super(AdmixtureWriter, self).__init__(wideobj, filename_suffix)
        self.__Q_file = self.filename_prefix.with_suffix(f".{self.wideobj.n_ancestries}.Q")
        self.__P_file = self.filename_prefix.with_suffix(f".{self.wideobj.n_ancestries}.P")

        self.__sample_id_file = self.filename_prefix.with_suffix(".sample_ids.txt") if self.wideobj.sample_IDs is not None else None
        self.__snp_file = self.filename_prefix.with_suffix(".snp_ids.txt") if self.wideobj.snps is not None else None
        self.__ancestry_file = self.filename_prefix.with_suffix(".map") if self.wideobj.ancestries is not None else None

    def write(self) -> None:
        self.filename_prefix.parent.mkdir(parents=True, exist_ok=True)
        self._write_Q()
        self._write_P()
        self._write_sample_ids()
        self._write_snps()
        self._write_ancestries()

    def _write_Q(self):
        np.savetxt(self.Q_file, self.wideobj.Q, delimiter=" ")
    
    def _write_P(self):
        np.savetxt(self.P_file, self.wideobj.P, delimiter=" ")
    
    def _write_sample_ids(self):
        if self.wideobj.sample_IDs is not None:
            np.savetxt(self.sample_id_file, self.wideobj.sample_IDs, fmt="%s")
    
    def _write_snps(self):
        if self.wideobj.snps is not None:
            np.savetxt(self.snp_file, self.wideobj.snps, fmt="%s")
    
    def _write_ancestries(self):
        if self.wideobj.ancestries is not None:
            np.savetxt(self.ancestry_file, self.wideobj.ancestries, fmt="%s")
    
    @property
    def Q_file(self) -> str:
        """Retrieve path to file to store the Q matrix

        Returns:
            str: path to file to store the Q matrix
        """
        return self.__Q_file
    
    @property
    def P_file(self) -> str:
        """Retrieve path to file to store the P matrix

        Returns:
            str: path to file to store the P matrix
        """
        return self.__P_file
    
    @property
    def sample_id_file(self) -> Union[str, None]:
        """Retrieve path to file to store the sample IDs

        Returns:
            str: path to file to store the sample IDs
        """
        return self.__sample_id_file
    
    @property
    def snp_file(self) -> Union[str, None]:
        """Retrieve path to file to store the SNP IDs

        Returns:
            str: path to file to store the SNP IDs
        """
        return self.__snp_file
    
    @property
    def ancestry_file(self) -> Union[str, None]:
        """Retrieve path to file to store the ancestry labels

        Returns:
            str: path to file to store the ancestry labels
        """
        return self.__ancestry_file
