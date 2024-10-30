import abc

class UKBPhenotypeObject(abc.ABC):
    """
    Abstract class for Phenotype data.
    """
    
    def __init__(self, 
                 sample_IDs, 
                 n_samples, 
                 cases_IDs, 
                 n_cases, 
                 controls_IDs, 
                 n_controls, 
                 all_haplotypes, 
                 cases_haplotypes, 
                 controls_haplotypes):

        self.__sample_IDs = sample_IDs
        self.__n_samples = n_samples
        self.__cases_IDs = cases_IDs
        self.__n_cases = n_cases
        self.__controls_IDs = controls_IDs
        self.__n_controls = n_controls
        self.__all_haplotypes = all_haplotypes
        self.__cases_haplotypes = cases_haplotypes
        self.__controls_haplotypes = controls_haplotypes

    @property
    def sample_IDs(self) -> list:
        """
        Retrieve IDs of samples

        Returns:
            list: IDs of samples
        """
        return self.__sample_IDs
    
    @property
    def n_samples(self) -> int:
        """
        Retrieve number of samples

        Returns:
            int: number of samples
        """
        return self.__n_samples
    
    @property
    def cases_IDs(self) -> list:
        """
        Retrieve IDs of cases

        Returns:
            list: IDs of cases
        """
        return self.__cases_IDs
    
    @property
    def n_cases(self) -> int:
        """
        Retrieve number of cases

        Returns:
            int: number of cases
        """
        return self.__n_cases
    
    @property
    def controls_IDs(self) -> list:
        """
        Retrieve IDs of controls

        Returns:
            list: IDs of controls
        """
        return self.__controls_IDs
    
    @property
    def n_controls(self) -> int:
        """
        Retrieve number of controls

        Returns:
            int: number of controls
        """
        return self.__n_controls
    
    @property
    def all_haplotypes(self) -> list:
        """
        Retrieve haplotypes of all samples

        Returns:
            list: haplotypes of all samples
        """
        return self.__all_haplotypes
    
    @property
    def cases_haplotypes(self) -> list:
        """
        Retrieve haplotypes of cases

        Returns:
            list: haplotypes of cases
        """
        return self.__cases_haplotypes
    
    @property
    def controls_haplotypes(self) -> list:
        """
        Retrieve haplotypes of controls

        Returns:
            list: haplotypes of controls
        """
        return self.__controls_haplotypes