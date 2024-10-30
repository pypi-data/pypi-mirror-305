import abc

class LAIBaseReader(abc.ABC):
    """
    Abstract class for local ancestry readers
    """ 

    def __init__(self, filename):
        self._filename = filename
    

    @abc.abstractmethod
    def read(self) -> None:
        pass

    @abc.abstractmethod
    def get_samples(self) -> list:
        pass
    
    @property
    def filename(self) -> str:
        """Retrieve path to file storing LAI info

        Returns:
            str: path to file storing LAI info
        """
        return self._filename
    