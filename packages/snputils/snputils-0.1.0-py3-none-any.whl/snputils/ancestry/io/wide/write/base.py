import abc
from pathlib import Path
from typing import Union

from snputils.ancestry.genobj.wide import WideAncestryObject


class BaseWideWriter(abc.ABC):
    """
    Abstract class for Wide (Global) Ancestry writers
    """ 

    def __init__(self, wideobj: WideAncestryObject, filename_prefix: Union[str, Path]):
        """Constructor

        Args:
            wideobj (WideAncestryObject): wide ancestry object
            filename_prefix (str): filename suffix (including parent directories) to store wide/global ancestry info. E.g., if "parent1/parent2/fname" is provided, the Q matrix will be stored as "parent1/parent2/fname.K.Q" and the P matrix will be stored as "parent1/parent2/fname.K.P", where K is the number of ancestries.
        """
        self._wideobj = wideobj
        self._filename_prefix = Path(filename_prefix)


    @abc.abstractmethod
    def write(self) -> None:
        pass
    
    @property
    def wideobj(self) -> WideAncestryObject:
        """
        Retrieve wide ancestry object instance

        Returns:
            WideAncestryObject: wide ancestry object instance
        """
        return self._wideobj
    
    @property
    def filename_prefix(self) -> str:
        """
        Retrieve filename suffix (including parent directories) to store wide/global ancestry info

        Returns:
            str: file format storing wide/global ancestry info
        """
        return self._filename_prefix
