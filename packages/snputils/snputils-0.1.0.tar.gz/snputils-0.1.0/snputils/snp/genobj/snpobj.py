import logging
import numpy as np
import copy
import warnings
import re
from typing import Optional, List, Tuple, Any

from ..._utils._process import (
    _match_to_replace,
    _correct_snp_flips,
    _get_chromosome_number
)

log = logging.getLogger(__name__)

class SNPObject:
    """
    Abstract class for Single Nucleotide Polymorphism exploitation.
    """
    def __init__(self,
                 calldata_gt: np.ndarray,
                 samples: Optional[np.ndarray] = None,
                 variants_ref: Optional[np.ndarray] = None,
                 variants_alt: Optional[np.ndarray] = None,
                 variants_chrom: Optional[np.ndarray] = None,
                 variants_filter_pass: Optional[np.ndarray] = None,
                 variants_id: Optional[np.ndarray] = None,
                 variants_pos: Optional[np.ndarray] = None,
                 variants_qual: Optional[np.ndarray] = None) -> None:
        """
        Initialize the SNPObject.

        Args:
            calldata_gt: An array containing the genotypes.
            samples: An array containing the sample IDs, or None if no samples are available.
            variants_ref: An array containing the reference of each SNP.
            variants_alt: An array containing the alternate alleles of each SNP.
            variants_chrom: An array containing the chromosome of each SNP.
            variants_filter_pass: An array containing flag for passed/failed control checks for each SNP.
            variants_id: An array containing SNP IDs.
            variants_pos: An array containing the position of each SNP in the chromosome.
            variants_qual: An array containing the Phred-scaled quality score for each SNP.
        """
        self.__calldata_gt = calldata_gt
        self.__samples = samples
        self.__variants_ref = variants_ref
        self.__variants_alt = variants_alt
        self.__variants_chrom = variants_chrom
        self.__variants_filter_pass = variants_filter_pass
        self.__variants_id = variants_id
        self.__variants_pos = variants_pos
        self.__variants_qual = variants_qual

    def copy(self):
        """
        Create and return a copy of the SNPObject.

        Returns:
            SNPObject: A copy of the SNPObject.
        """
        return copy.deepcopy(self)

    def __getitem__(self, key: str) -> Any:
        """
        Enables dictionary-like access to class attributes.

        Args:
            key (str): The attribute key to access.

        Returns:
            Any: The value associated with 'key'.

        Raises:
            KeyError: If 'key' does not correspond to an attribute.
        """
        try:
            return getattr(self, key)
        except:
            raise KeyError(f'Invalid key: {key}.')

    def __setitem__(self, key: str, value: Any):
        """
        Enables setting class attributes using dictionary-like square bracket notation.

        Args:
            key (str): The attribute key to set.
            value (Any): The value to assign to the attribute.

        Raises:
            KeyError: If 'key' does not correspond to an attribute.
        """
        try:
            setattr(self, key, value)
        except:
            raise KeyError(f'Invalid key: {key}.')

    def keys(self) -> List[str]:
        """
        Returns the list of attribute names, with internal identifiers removed.

        Returns:
            List[str]: A cleaned list of attribute names.
        """
        return [attr.replace('_SNPObject__', '') for attr in vars(self)]

    @property
    def calldata_gt(self) -> np.ndarray:
        """
        Retrieve the genotypes array.

        Returns:
            np.ndarray: An array containing the genotypes.
        """
        return self.__calldata_gt
    
    @calldata_gt.setter
    def calldata_gt(self, x: np.ndarray):
        """
        Update `calldata_gt`.

        Args:
            x: The new value for `calldata_gt`.
        """
        self.__calldata_gt = x

    @property
    def samples(self) -> Optional[np.ndarray]:
        """
        Retrieve samples array.

        Returns:
            np.ndarray or None: Array containing the sample IDs, or None if no samples are available.
        """
        return self.__samples
    
    @samples.setter
    def samples(self, x: np.ndarray):
        """
        Update `samples`.

        Args:
            x: The new value for `samples`.
        """
        self.__samples = x

    @property
    def variants_ref(self) -> Optional[np.ndarray]:
        """
        Retrieve the reference array.

        Returns:
            np.ndarray: An array containing the reference of each SNP.
        """
        return self.__variants_ref

    @variants_ref.setter
    def variants_ref(self, x: np.ndarray):
        """
        Update `variants_ref`.

        Args:
            x: The new value for `variants_ref`.
        """
        self.__variants_ref = x

    @property
    def variants_alt(self) -> Optional[np.ndarray]:
        """
        Retrieve the array of alternate alleles.

        Returns:
            np.ndarray: Array containing the alternate alleles of each SNP.
        """
        return self.__variants_alt

    @variants_alt.setter
    def variants_alt(self, x: np.ndarray):
        """
        Update `variants_alt`.

        Args:
            x: The new value for `variants_alt`.
        """
        self.__variants_alt = x

    @property
    def variants_chrom(self) -> Optional[np.ndarray]:
        """
        Retrieve the array of chromosomes.

        Returns:
            np.ndarray: An array containing the chromosome of each SNP.
        """
        return self.__variants_chrom
    
    @variants_chrom.setter
    def variants_chrom(self, x: np.ndarray):
        """
        Update `variants_chrom`.

        Args:
            x: The new value for `variants_chrom`.
        """
        self.__variants_chrom = x

    @property
    def variants_filter_pass(self) -> Optional[np.ndarray]:
        """
        Retrieve filter pass array.

        Returns:
            np.ndarray: Array containing flag for passed/failed control checks for each SNP.
        """
        return self.__variants_filter_pass
    
    @variants_filter_pass.setter
    def variants_filter_pass(self, x: np.ndarray):
        """
        Update `variants_filter_pass`.

        Args:
            x: The new value for `variants_filter_pass`.
        """
        self.__variants_filter_pass = x

    @property
    def variants_id(self) -> Optional[np.ndarray]:
        """
        Retrieve variants ID array.

        Returns:
            np.ndarray: Array containing SNP IDs.
        """
        return self.__variants_id

    @variants_id.setter
    def variants_id(self, x: np.ndarray):
        """
        Update `variants_id`.

        Args:
            x: The new value for `variants_id`.
        """
        self.__variants_id = x

    @property
    def variants_pos(self) -> Optional[np.ndarray]:
        """
        Retrieve variant positions array.

        Returns:
            np.ndarray: Array containing the position of each SNP in the chromosome.
        """
        return self.__variants_pos

    @variants_pos.setter
    def variants_pos(self, x: np.ndarray):
        """
        Update `variants_pos`.

        Args:
            x: The new value for `variants_pos`.
        """
        self.__variants_pos = x

    @property
    def variants_qual(self) -> Optional[np.ndarray]:
        """
        Retrieve variants quality array.

        Returns:
            np.ndarray: Array containing the Phred-scaled quality score for each SNP.
        """
        return self.__variants_qual
    
    @variants_qual.setter
    def variants_qual(self, x: np.ndarray):
        """
        Update `variants_qual`.

        Args:
            x: The new value for `variants_qual`.
        """
        self.__variants_qual = x

    def n_samples(self) -> int:
        """
        Retrieve the number of samples.

        Returns:
            int: The number of samples.
        """
        return self.__calldata_gt.shape[1]

    def n_snps(self) -> int:
        """
        Retrieve the number of SNPs.

        Returns:
            int: The number of SNPs.
        """
        return self.__calldata_gt.shape[0]

    def unique_chrom(self) -> np.ndarray:
        """
        Retrieve unique chromosome names, preserving their order of appearance.

        Returns:
            np.ndarray: The unique chromosome names.

        Raises:
            ValueError: If no chromosome data is available.
        """
        if self.variants_chrom is not None:
            # Identify unique chromosome names and their first indices of occurrence
            _, idx = np.unique(self.variants_chrom, return_index=True)
            # Return chromosome names sorted by their first occurrence to maintain original order
            return self.variants_chrom[np.sort(idx)]
        else:
            raise ValueError("No chromosome data is available.")

    def rename_chrom(self, to_replace={'^([0-9]+)$': r'chr\1', r'^chr([0-9]+)$': r'\1'},
                     value=None, regex=True, inplace=False):
        """
        Replaces chromosome values in the SNPObject.

        Args:
            to_replace: By default, the notation will change from `<chrom_num>` to
                `chr<chrom_num>` or vice-versa. If a chromosome is in neither of these formats, its notation will remain untouched.
                - If str or list of str, then any exact string matches will be replaced with `value`.
                - If regex, then the first match will be replaced with `value`.
                - If dict, then any exact string matches of the keys will be replaced with the corresponding value.
            value: - If `to_replace` is a list or a str and `value` is provided, the
                matching values will be replaced with this value.
                - If `to_replace` is a dictionary, `value` should be None.
            regex: A boolean flag indicating whether `to_replace` is a dictionary of regular expressions.
            inplace: If True, modifies self in place. Otherwise, return a new SNPObject with the changes.

        Returns:
            SNPObject or None: If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.
        """
        # Change input format to dictionary where keys are old values to replace
        # and values are the new values to adopt
        if isinstance(to_replace, (str, int)):
            to_replace = [to_replace]
        if isinstance(value, (str, int)):
            value = [value]
        if isinstance(to_replace, list) and isinstance(value, list):
            dictionary = dict(zip(to_replace, value))
        elif isinstance(to_replace, dict) and value is None:
            dictionary = to_replace
        else:
            raise ValueError("The type of both to_replace and value should be "
                             "str, list of str, dict or have the same type.")

        # To replace values in numpy array with _match_to_replace
        vec_replace_values = np.vectorize(_match_to_replace)

        if inplace:
            self.variants_chrom = vec_replace_values(self.variants_chrom, dictionary, regex)
            return None
        else:
            snpobj = self.copy()
            snpobj.variants_chrom = vec_replace_values(self.variants_chrom, dictionary, regex)
            return snpobj
        
    def rename_missings(self, before=-1, after=".", inplace=False):
        """
        Replaces missing values in the 'calldata_gt' field.

        By default, replaces missing value -1 with ".".

        Args:
            before: Missing value before replacement. Defaults to -1.
            after: Missing value after replacement. Defaults to ".".
            inplace: If True, modifies self in place. Otherwise, return a new SNPObject with the changes.

        Returns:
            SNPObject or None: If inplace=False, returns the modified object.
                Otherwise, the operation is done in-place and None is returned.
        """
        if inplace:
            self['calldata_gt'] = np.where(self['calldata_gt'] == before, after, self['calldata_gt']) 
            return None
        else:
            snpobj = self.copy()
            snpobj['calldata_gt'] = np.where(snpobj['calldata_gt'] == before, after, snpobj['calldata_gt']) 
            return snpobj

    def filter_snps(self, chrom=None, pos=None, indexes=None, include=True, inplace=False):
        """
        Filter SNPs according to chromosome name and/or SNP position, or based
        on SNP indexes (considering all chromosomes). It can either include or
        exclude SNPs that match the specified criteria.

        Args:
            chrom: Chromosomes to filter SNPs by.
            pos: Positions to filter SNPs by.
            indexes: Indexes of SNPs to include or exclude.
            include: If True, includes SNPs that match the specified criteria,
                otherwise excludes them.
            inplace: If True, modifies self in place. Otherwise, return a new SNPObject with the changes.

        Returns:
            SNPObject or None: If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.

        Raises:
            ValueError: If indexes are provided when chrom or pos are specified.

        Warnings:
            If none of chrom, pos, or indexes are provided.
        """
        # Change input format to list
        if isinstance(chrom, (str, int)):
            chrom = [chrom]
        elif isinstance(chrom, (np.ndarray)):
            chrom = list(chrom)
        if isinstance(pos, (int)):
            pos = [pos]
        elif isinstance(pos, (np.ndarray)):
            pos = list(pos)
        if isinstance(indexes, (int)):
            indexes = [indexes]
        elif isinstance(indexes, (np.ndarray)):
            indexes = list(indexes)

        if indexes is not None:
            if chrom or pos:
                raise ValueError("Indexes should not be provided when chrom "
                                    "or pos are specified.")
            else:
                # Create vector of booleans with as many positions as SNPs
                # The provided indexes are set to True
                arr = np.zeros(self.n_snps(), dtype=bool)
                arr[indexes] = True
                indexes = arr
        elif chrom and pos:
            indexes = np.in1d(self.variants_chrom, chrom) &\
                np.in1d(self.variants_pos, pos)
        elif chrom:
            indexes = np.in1d(self.variants_chrom, chrom)
        elif pos:
            indexes = np.in1d(self.variants_pos, pos)
        elif not indexes:
            warnings.warn("At least one of chrom, pos or indexes should be provided.")

        keys = ['calldata_gt', 'variants_ref', 'variants_alt',
                'variants_chrom', 'variants_filter_pass', 'variants_id',
                'variants_pos', 'variants_qual']

        if not include:
            # Invert boolean array from True to False and vice-versa
            indexes = np.invert(indexes)

        if inplace:
            for key in keys:
                if self[key] is not None:
                    self[key] = np.asarray(self[key][indexes])
            return None
        else:
            snpobj = self.copy()
            for key in keys:
                if snpobj[key] is not None:
                    snpobj[key] = np.asarray(snpobj[key][indexes])
            return snpobj

    def filter_samples(self, samples=None, indexes=None, include=True, inplace=False):
        """
        Filter samples according to 'samples' names, or based on sample 'indexes'.
        It can either include or exclude samples that match the specified
        criteria.

        Args:
            samples: Samples to filter data by.
            indexes: Indexes of samples to include or exclude.
            include: If True, includes samples that match the specified criteria,
                otherwise excludes them.
            inplace: If True, modifies self in place. Otherwise, return a new SNPObject with the changes.

        Returns:
            SNPObject or None: If inplace=False, return the modified object. Otherwise, the
                operation is done in-place and None is returned.

        Raises:
            ValueError: If both samples and indexes are provided.
            UserWarning: If neither samples nor indexes are provided.

        """
        if samples is not None:
            # Get the indices of the specified sample names
            sample_names = np.asarray(self['samples'])
            indexes = np.where(np.isin(sample_names, samples))[0]
        elif indexes is not None:
            indexes = np.asarray(indexes)
        else:
            raise ValueError("Either 'samples' or 'indexes' must be provided for filtering.")

        if not include:
            # Exclude the specified samples or indices
            all_indices = np.arange(len(self['samples']))
            indexes = np.setdiff1d(all_indices, indexes)

        if inplace:
            if self['samples'] is not None:
                self['samples'] = np.asarray(self['samples'])[indexes]
            if self['calldata_gt'] is not None:
                self['calldata_gt'] = np.asarray(self['calldata_gt'])[:, indexes, :]
            return None
        else:
            snpobj = self.copy()
            if snpobj['samples'] is not None:
                snpobj['samples'] = np.asarray(snpobj['samples'])[indexes]
            if self['calldata_gt'] is not None:
                snpobj['calldata_gt'] = np.asarray(self['calldata_gt'])[:, indexes, :]
            return snpobj

    def subset_to_common_snps(self, snpobj: 'SNPObject') -> 'SNPObject':
        """
        Subset the current SNPObject (query) to contain only the common markers 
        (i.e., SNPs at the same CHROM, POS, REF and ALT) with the provided 
        SNPObject (reference).

        Args:
            snpobj: Another SNPObject instance to subset common markers with.
            
        Returns:
            SNPObject: The modified SNPObject containing only the common markers.
        """
        indexes = []  # Indexes of common markers in query
        
        i = 0  # Iterator for query
        j = 0  # Iterator for reference
        
        while i < len(self['variants_pos']) and j < len(snpobj['variants_pos']):
            # Extract chromosome number from query at index i
            if self['variants_chrom'][i].isdigit():
                chrom = int(self['variants_chrom'][i])
            else:
                match = re.search(r'\d+', self['variants_chrom'][i])
                if match:
                    chrom = int(match.group())
                else:
                    raise ValueError(f"No numeric chromosome found in '{self['variants_chrom'][i]}'")

            # Extract chromosome number from snpobj at index j
            if snpobj['variants_chrom'][j].isdigit():
                chrom_snpobj = int(snpobj['variants_chrom'][j])
            else:
                match = re.search(r'\d+', snpobj['variants_chrom'][j])
                if match:
                    chrom_snpobj = int(match.group())
                else:
                    raise ValueError(f"No numeric chromosome found in '{snpobj['variants_chrom'][j]}'")

            if chrom < chrom_snpobj:
                i += 1
            elif chrom > chrom_snpobj:
                j += 1
            elif self['variants_pos'][i] < snpobj['variants_pos'][j]:
                # If the position of the SNP in query is smaller than in snpobj...
                i += 1
            elif self['variants_pos'][i] > snpobj['variants_pos'][j]:
                # If the position of the SNP in query is larger than in snpobj...
                j += 1
            else:
                # Found a SNP at the same position...
                if (self['variants_ref'][i] == snpobj['variants_ref'][j] and 
                    self['variants_alt'][i][0] == snpobj['variants_alt'][j][0]):
                    # If reference and alternate alleles match between datasets...
                    # Save index of common SNP in query
                    indexes.append(i)

                # Move both iterators forward
                i += 1
                j += 1

        # Filter and return the common SNPs
        return self.filter_snps(indexes=indexes, include=True, inplace=False)

    def remove_strand_ambiguous_snps(self, inplace=False):
        """
        Search and remove strand-ambiguous SNPs. A/T, T/A, C/G, and G/C pairs 
        are strand-ambiguous because their components are complementary, making 
        it difficult to determine the DNA strand.
        
        Args:
            remove: Weather to remove ambiguous snps.
            inplace: If True, modifies self in place. Otherwise, return a new SNPObject with the changes.
            
        Returns:
        SNPObject or None
            If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.
        """
        non_ambiguous_idx = [] # Empty list to store indexes of non-ambiguous SNPs
    
        A_T_count = 0  # Counter of A/T ambiguities
        T_A_count = 0  # Counter of T/A ambiguities
        C_G_count = 0  # Counter of C/G ambiguities
        G_C_count = 0  # Counter of G/C ambiguities

        # Obtain REF and ALT from query
        REF = self['variants_ref']
        ALT = self['variants_alt']
        
        # Check if each SNP is strand-ambiguous
        for i in range (0, len(REF)):
            if REF[i] == 'A' and ALT[i][0] == 'T':
                # Strand-ambiguous SNP of A/T type
                A_T_count += 1
            elif REF[i] == 'T' and ALT[i][0] == 'A':
                # Strand-ambiguous SNP of T/A type
                T_A_count += 1
            elif REF[i] == 'C' and ALT[i][0] == 'G':
                # Strand-ambiguous SNP of C/G type
                C_G_count += 1
            elif REF[i] == 'G' and ALT[i][0] == 'C':
                # Strand-ambiguous SNP of G/C type
                G_C_count += 1
            else:
                # The SNP at index i is not ambiguous
                non_ambiguous_idx.append(i)

        log.info(f'{A_T_count} ambiguities of A-T type.')
        log.info(f'{T_A_count} ambiguities of T-A type.')
        log.info(f'{C_G_count} ambiguities of C-G type.')
        log.info(f'{G_C_count} ambiguities of G-C type.')
        log.info(f'{A_T_count+T_A_count+C_G_count+G_C_count} strand-ambiguous SNPs in total.')
        
        # Keep the SNPs that are not strand-ambiguous and remove the rest
        log.debug('Removing all amgiguities.')
        if inplace:
            return self.filter_snps(indexes=non_ambiguous_idx, include=True, inplace=True)
        else:
            snpobj = self.copy()
            snpobj = snpobj.filter_snps(indexes=non_ambiguous_idx, include=True, inplace=False)
            return snpobj
        

    def get_common_variants_intersection(self, snpobj: 'SNPObject', index_by: str = 'pos'): # TODO: it has a bug that makes it fail if there are repited positions!!
        if index_by == 'pos':
            query_identifiers = [f"{chrom}-{pos}" for chrom, pos in zip(self['variants_chrom'], self['variants_pos'])]
            reference_identifiers = [f"{chrom}-{pos}" for chrom, pos in zip(snpobj['variants_chrom'], snpobj['variants_pos'])]
        elif index_by == 'id':
            query_identifiers = self['variants_id'].tolist()
            reference_identifiers = snpobj['variants_id'].tolist()
        elif index_by == 'pos+id':
            query_identifiers = [f"{chrom}-{pos}-{ids}" for chrom, pos, ids in zip(self['variants_chrom'].tolist(), self['variants_pos'].tolist(), self['variants_id'].tolist())]
            reference_identifiers = [f"{chrom}-{pos}-{ids}" for chrom, pos, ids in zip(snpobj['variants_chrom'].tolist(), snpobj['variants_pos'].tolist(), snpobj['variants_id'].tolist())]
        else:
            raise ValueError("index_by must be either 'pos' or 'id'")
        
        # Convert to sets for intersection
        query_set = set(query_identifiers)
        reference_set = set(reference_identifiers)
        
        # Find common elements
        common_ids = query_set.intersection(reference_set)
        
        # Map back to indices (the part that reintroduces loops)
        query_idx = [i for i, id in enumerate(query_identifiers) if id in common_ids]
        reference_idx = [i for i, id in enumerate(reference_identifiers) if id in common_ids]
        
        return list(common_ids), np.array(query_idx), np.array(reference_idx)

    def correct_snp_flips(self, snpobj: 'SNPObject', inplace: bool = False, log_correct_stats: bool = True, check_complement: bool = True, index_by: str = 'pos', common_variants_intersection: Optional[Tuple[np.ndarray, np.ndarray]] = None) -> Optional['SNPObject']:
        """
        Identifies and corrects SNPs where REF and ALT alleles are swapped between
        the query and reference SNP objects. Operates either in-place or returns a modified copy.
        
        Parameters
        ----------
        snpobj : SNPObject
            The reference SNPObject instance for comparison.
        inplace : bool, optional
            If True, modifies self in place. Otherwise, return a new SNPObject with the changes.
        log_correct_stats : bool, optional
            If True, logs statistical information about matches and corrections. Default is True.
        check_complement : bool, optional
            If True, checks both exact matches and complementary base pairs (e.g., A<->T and C<->G) when identifying swapped SNPs. Default is True.
        index_by : str, optional
            Determines whether to index SNPs by 'pos' (chromosome-position) or 'id'. Default is 'pos'.
        common_variants_intersection : tuple of arrays, optional
            Precomputed indices that correspond to the intersection of common variants between the query and reference SNP objects. If None, the intersection is computed within the function.

        Returns
        -------
        SNPObject or None
            Returns a modified SNPObject if `inplace` is False. Returns None if `inplace` is True and modifications were made in-place.
        """
        # Define complement mappings for A, C, G, T
        complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

        # Function to get complement of a base
        def get_complement(base):
            return complement_map.get(base, base) 

        # Get common variants' intersection
        if common_variants_intersection != None:
            query_idx, reference_idx = common_variants_intersection
        else:
            _, query_idx, reference_idx = self.get_common_variants_intersection(snpobj, index_by=index_by)

        if log_correct_stats:
            matching_ref = np.sum(self['variants_ref'][query_idx] == snpobj['variants_ref'][reference_idx])
            matching_alt = np.sum(self['variants_alt'][query_idx, 0] == snpobj['variants_alt'][reference_idx, 0])
            ambiguous = np.sum(self['variants_ref'][query_idx] == self['variants_alt'][query_idx, 0])

            log.info(f"Matching ref and alts are: {matching_ref}, {matching_alt}")
            log.info(f"Number of ambiguous is {ambiguous}")

        # Identify indices where REF and ALT alleles are swapped
        if not check_complement:
            swapped_ref = (self['variants_ref'][query_idx] == snpobj['variants_alt'][reference_idx, 0])
            swapped_alt = self['variants_alt'][query_idx, 0] == snpobj['variants_ref'][reference_idx]
            not_ambiguous = self['variants_ref'][query_idx] != self['variants_alt'][query_idx, 0]
        else:
            # Check if REF and ALT alleles are swapped or their complements are swapped
            swapped_ref = (self['variants_ref'][query_idx] == snpobj['variants_alt'][reference_idx, 0]) | \
                        (np.vectorize(get_complement)(self['variants_ref'][query_idx]) == snpobj['variants_alt'][reference_idx, 0])
            swapped_alt = (self['variants_alt'][query_idx, 0] == snpobj['variants_ref'][reference_idx]) | \
                        (np.vectorize(get_complement)(self['variants_alt'][query_idx, 0]) == snpobj['variants_ref'][reference_idx])
            not_ambiguous = self['variants_ref'][query_idx] != self['variants_alt'][query_idx, 0]

        flip_idx_query = query_idx[swapped_ref & swapped_alt & not_ambiguous]

        if len(flip_idx_query) > 0:
            log.info(f'Correcting {len(flip_idx_query)} SNP flips.')

            # Correct the SNP flips based on whether the operation is in-place or not
            if inplace:
                #_correct_snp_flips(self, flip_idx_query)
                temp_alts = self['variants_alt'][flip_idx_query, 0]
                temp_refs = self['variants_ref'][flip_idx_query]
                self['variants_alt'][flip_idx_query, 0] = temp_refs
                self['variants_ref'][flip_idx_query] = temp_alts
                self['calldata_gt'][flip_idx_query] = 1 - self['calldata_gt'][flip_idx_query]
                return None
            else:
                new_snpobj = self.copy()
                new_snpobj = _correct_snp_flips(new_snpobj, flip_idx_query)
                return new_snpobj
        else:
            log.info('No SNP flips found to correct.')
            return self if not inplace else None

    def remove_mismatching_snps(self, snpobj: 'SNPObject', inplace: bool = False) -> Optional['SNPObject']:
        """
        Search and remove mismatching SNPs in the current object (query)
        with respect to the provided snpobj (reference). A variant mismatch is a 
        difference in the variants/REF or variants/ALT fields between SNPs at the 
        same chromosome and position in the query and reference datasets.

        Args:
        snpobj:
           Another SNPObject instance to search for SNP mismatches.
        inplace:
            If True, modifies self in place. Otherwise, return a new SNPObject with the changes.
           
        Returns:
            If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.
        """
        # Define counter of SNPs that are at the same position
        n_coincidences = 0

        # Empty list to store the indexes of the SNPs that contain a SNP 
        # mismatch in the query
        mismatch_idx_query = []

        i = 0  # Reference iterator
        j = 0  # Query iterator

        while i < len(snpobj['variants_pos']) and j < len(self['variants_pos']):
            # Obtain the chromosome number for the i-th SNP in the reference
            chrom_ref = _get_chromosome_number(snpobj['variants_chrom'][i])

            # Obtain the chromosome number for the j-th SNP in the query
            chrom_query = _get_chromosome_number(self['variants_chrom'][j])

            if chrom_ref < chrom_query:
                i += 1
            elif chrom_ref > chrom_query:
                j += 1
            else:
                if snpobj['variants_pos'][i] < self['variants_pos'][j]:
                    # If the position of the SNP in the reference dataset is smaller than the 
                    # position of the SNP in the query dataset...
                    # Move to the next SNP in the reference
                    i += 1
                elif snpobj['variants_pos'][i] > self['variants_pos'][j]:
                    # If the position of the SNP in the query dataset is smaller than the 
                    # position of the SNP in the reference dataset...
                    # Move to the next SNP in the query
                    j += 1
                else:
                    # Found a SNP at the same position...
                    # Search if the SNP is mismatching
                    if (snpobj['variants_ref'][i] != self['variants_ref'][j] or 
                        snpobj['variants_alt'][i,0] != self['variants_alt'][j,0]):
                        # The SNP is mismatching
                        mismatch_idx_query.append(j)

                    # Increase the counter of coincidences and the iterator for both datasets
                    n_coincidences += 1
                    i += 1
                    j += 1
        
        log.info(f'{n_coincidences} SNPs at the same position.')
        log.info(f'{len(mismatch_idx_query)} mismatching SNPs in total.')

        # Remove mismatching SNPs
        log.debug('Removing all SNP mismatches.')
        if inplace:
            return self.filter_snps(indexes=mismatch_idx_query, include=False, inplace=True)
        else:
            snpobj = self.copy()
            snpobj = snpobj.filter_snps(indexes=mismatch_idx_query, include=False, inplace=False)
            return snpobj

    def set_empty_to_missing(self, inplace: bool = False):
        """
        Set empty string '' to missing '.'.

        Args:
            inplace:
                A boolean flag that controls the behavior of the method. If True,
                the operation is done in-place and the original object is modified,
                otherwise, a new object is created and returned.

        Returns:
            If inplace=False, return the modified object. Otherwise, the
            operation is done in-place and None is returned.
        """
        if inplace:
            if self.variants_alt is not None:
                self.variants_alt[:, 0][self.variants_alt[:, 0] == ''] = '.'
            if self.variants_ref is not None:
                self.variants_ref[self.variants_ref == ''] = '.'
            if self.variants_qual is not None:
                self.variants_qual = self.variants_qual.astype(str)
                self.variants_qual[(self.variants_qual == '') | (self.variants_qual == 'nan')] = '.'
            if self.variants_chrom is not None:
                self.variants_chrom = self.variants_chrom.astype(str)
                self.variants_chrom[self.variants_chrom == ''] = '.'
            if self.variants_filter_pass is not None:
                self.variants_filter_pass[self.variants_filter_pass == ''] = '.'
            if self.variants_id is not None:
                self.variants_id[self.variants_id == ''] = '.'
            return self
        else:
            snpobj = self.copy()
            if snpobj.variants_alt is not None:
                snpobj.variants_alt[:, 0][snpobj.variants_alt[:, 0] == ''] = '.'
            if snpobj.variants_ref is not None:
                snpobj.variants_ref[snpobj.variants_ref == ''] = '.'
            if snpobj.variants_qual is not None:
                snpobj.variants_qual = snpobj.variants_qual.astype(str)
                snpobj.variants_qual[(snpobj.variants_qual == '') | (snpobj.variants_qual == 'nan')] = '.'
            if snpobj.variants_chrom is not None:
                snpobj.variants_chrom[snpobj.variants_chrom == ''] = '.'
            if snpobj.variants_filter_pass is not None:
                snpobj.variants_filter_pass[snpobj.variants_filter_pass == ''] = '.'
            if snpobj.variants_id is not None:
                snpobj.variants_id[snpobj.variants_id == ''] = '.'
            return snpobj

    def shuffle_positions(self, inplace=False):
        """
        Randomly shuffles the positions of the variants in the SNPObject, 
        along with their corresponding data in calldata_gt and other attributes.

        Parameters
        ----------
        inplace : bool, default=False
            If True, modify self in place. Otherwise, return a new SNPObject with the changes.

        Returns
        -------
        SNPObject or None
            If inplace=False, return a shuffled copy of the SNPObject. 
            If inplace=True, the shuffling is done in-place and returns None.
        """
        # Generate a random permutation index
        shuffle_index = np.random.permutation(self.n_snps())

        # Apply shuffling to all relevant attributes using the class's dictionary-like interface
        if inplace:
            for key in self.keys():
                if self[key] is not None:
                    if key == 'calldata_gt':
                        # calldata_gt has a different shape, so it's shuffled along axis 0
                        self[key] = self[key][shuffle_index, ...]
                    elif 'variant' in key:
                        # Other attributes are 1D arrays
                        self[key] = np.asarray(self[key])[shuffle_index]
            return None
        else:
            shuffled_snpobj = self.copy()
            for key in shuffled_snpobj.keys():
                if shuffled_snpobj[key] is not None:
                    if key == 'calldata_gt':
                        shuffled_snpobj[key] = shuffled_snpobj[key][shuffle_index, ...]
                    elif 'variant' in key:
                        shuffled_snpobj[key] = np.asarray(shuffled_snpobj[key])[shuffle_index]
            return shuffled_snpobj

    def detect_chromosome_format(self):
        """
        Detects the prefix formatting of a given chromosome string.

        Parameters
        ----------
        chromosome_str : str
            The chromosome string to check.

        Returns
        -------
        str
            The prefix of the chromosome string if the format is recognized, otherwise 'Unknown'.
        """
        chromosome_str = self.unique_chrom()[0]

        # Regular expressions for different chromosome formats
        patterns = {
            'chr': r'^chr(\d+|X|Y)$',
            'chm': r'^chm(\d+|X|Y)$',
            'chrom': r'^chrom(\d+|X|Y)$',
            'plain': r'^(\d+|X|Y)$'
        }
        
        for prefix, pattern in patterns.items():
            if re.match(pattern, chromosome_str):
                return prefix
        
        return "Unknown format"

    def convert_chromosome_format(self, from_format: str, to_format: str, inplace=False):
        """
        Converts chromosome naming formats from one specified format to another.

        Parameters
        ----------
        self : SNPObject
            The object containing chromosome data to be converted.
        from_format : str
            The current format of the chromosome data ('chr', 'chm', 'chrom', 'plain'):
            - 'chr': 'chr1', 'chr2', ..., 'chrX', 'chrY', 'chrM'.
            - 'chm': 'chm1', 'chm2', ..., 'chmX', 'chmY', 'chmM'.
            - 'chrom': 'chrom1', 'chrom2', ..., 'chromX', 'chromY', 'chromM'.
            - 'plain': '1', '2', ..., 'X', 'Y', 'M'.
        to_format : str
            The desired format to which the chromosome data should be converted.
            Acceptable values are the same as `from_format` ('chr', 'chm', 'chrom', 'plain').
        inplace : bool, default=False
            If True, modify self in place. Otherwise, return a new SNPObject with the changes.

        Returns
        -------
        SNPObject or None
            A new SNPObject with converted chromosome naming formats if inplace is False, None otherwise.
        """
        # List of possible chromosome identifiers
        chrom_list = [*map(str, range(1, 23)), 'X', 'Y', 'M']  # M for mitochondrial chromosomes
        
        # Format mappings for different chromosome naming conventions
        format_mappings = {
            'chr': [f'chr{i}' for i in chrom_list],
            'chm': [f'chm{i}' for i in chrom_list],
            'chrom': [f'chrom{i}' for i in chrom_list],
            'plain': chrom_list,
        }

        # Verify that from_format and to_format are valid
        if from_format not in format_mappings or to_format not in format_mappings:
            raise ValueError(f"Invalid format: {from_format} or {to_format}. Must be one of {list(format_mappings.keys())}.")

        # Check if all chromosomes in the object match the expected from_format
        variants_chrom = self['variants_chrom'].astype(str)
        expected_chroms = set(format_mappings[from_format])
        mismatched_chroms = set(variants_chrom) - expected_chroms

        if mismatched_chroms:
            raise ValueError(f"The following chromosomes do not match the from_format '{from_format}': {mismatched_chroms}")

        # Conditions for np.select
        conditions = [variants_chrom == chrom for chrom in format_mappings[from_format]]

        # Rename chromosomes based on inplace flag
        if inplace:
            self['variants_chrom'] = np.select(conditions, format_mappings[to_format], default='unknown')
            return None
        else:
            new_snp_object = self.copy()
            new_snp_object['variants_chrom'] = np.select(conditions, format_mappings[to_format], default='unknown')
            return new_snp_object

    def rename_chrom_from_snpobj(self, snpobj: 'SNPObject', inplace=False):
        """
        Renames the chromosome format in the current object (query) to match that of the 
        provided snpobj (reference).

        Parameters
        ----------
        self : SNPObject
            The object whose chromosome format will be changed.
        snpobj : SNPObject
            The object with the desired chromosome format.
        inplace : bool, default=False
            If True, modify self in place. Otherwise, return a new SNPObject with the changes.

        Returns
        -------
        SNPObject or None
            A new SNPObject with converted chromosome naming formats if inplace is False, None otherwise.
        """
        # Detect the chromosome formats of snpobj1 and snpobj2
        fmt1 = self.detect_chromosome_format()
        fmt2 = snpobj.detect_chromosome_format()

        # Convert the chromosome format of snpobj1 to match snpobj2
        if inplace:
            self.convert_chromosome_format(fmt1, fmt2, inplace=True)
            return None
        else:
            return self.convert_chromosome_format(fmt1, fmt2, inplace=False)
