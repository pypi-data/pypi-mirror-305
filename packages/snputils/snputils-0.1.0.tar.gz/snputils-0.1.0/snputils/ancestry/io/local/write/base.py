import abc
from snputils.ancestry.genobj.local import LocalAncestryObject

class LAIBaseWriter(abc.ABC):
    """
    Abstract class for Local Ancestry writers
    """ 

    def __init__(self, laiobj, filename):
        self._laiobj = laiobj
        self._filename = filename
    

    @abc.abstractmethod
    def write(self) -> None:
        pass
    
    @property
    def laiobj(self) -> LocalAncestryObject:
        """
        Retrieve LAI info

        Returns:
            LocalAncestryObject: LAI info
        """
        return self._laiobj
    
    @property
    def filename(self) -> str:
        """
        Retrieve path to file storing LAI info

        Returns:
            str: path to file storing LAI info
        """
        return self._filename
    