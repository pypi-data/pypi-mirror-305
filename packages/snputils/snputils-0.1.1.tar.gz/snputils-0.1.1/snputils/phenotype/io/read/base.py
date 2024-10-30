import abc

class PhenotypeBaseReader(abc.ABC):
    """
    Abstract class for Phenotype readers
    """ 

    def __init__(self, filename):
        self._filename = filename
    
    @abc.abstractmethod
    def read(self) -> None:
        pass
    
    @property
    def filename(self) -> str:
        """Retrieve path to file storing Phenotype info

        Returns:
            str: path to file storing Phenotype info
        """
        return self._filename