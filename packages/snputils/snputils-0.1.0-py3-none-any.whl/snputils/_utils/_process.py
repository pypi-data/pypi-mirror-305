import re
import numpy as np


def _match_to_replace(val, dictionary, regex):
    """
    Find the matching key in the provided `dictionary` for the given value `val` 
    so that it can be replaced with the corresponding value.

    Parameters
    ----------
    val : str, int, float
        The value to be matched and possibly replaced.
    dictionary : dict
        A dictionary containing the keys and values for matching and replacing. 
        The keys should be of the same data type as `val`.
    regex : bool, default=True
            A boolean flag indicating whether `to_replace` is a dictionary of 
            regular expressions.

    Returns
    -------
    str, int, float
        The value to replace. If no match is found, the original value is returned.
    """
    if regex:
        # Use regex expression to find the match
        for key, value in dictionary.items():
            if isinstance(key, str):
                match = re.match(key, val)
                if match:
                    # Return the value associated with the first matching
                    # regex expression with re.sub
                    return re.sub(key, value, val)
        # If the value does not match any regex expression,
        # return the original value
        return val
    else:
        # Return value associated to key in dictionary
        # If the key does not exist, return the original value
        return dictionary.get(val, val)
    

def _correct_snp_flips(snpobj, indexes):
    """
    Corrects all flipped SNPs at 'indexes' by swapping the REF and ALT fields.
    Consequently, the zeros and ones in the 'calldata_gt' field are also swapped.
    
    Parameters
    ----------
    snpobj : SNPObject
       An SNPObject instance.
        
    indexes : list
        Indexes of the SNPs in 'snpobj' with a flip.
    
    Returns
    -------
    SNPObject
        The modified object with corrected SNPs.
    """
    if len(indexes) > 0:
        # If there is a SNP flip...
        # Swap the REF and ALT fields
        ref_aux = snpobj['variants_ref'][indexes]
        alt_aux = snpobj['variants_alt'][indexes,0]
        snpobj['variants_ref'][indexes] = snpobj['variants_alt'][indexes,0]
        snpobj['variants_alt'][indexes,0] = ref_aux
        
        # Ensure the REF and the ALT were correctly swapped
        assert (snpobj['variants_alt'][indexes,0] == ref_aux).all(),\
        'The reference and the alternate were not swapped correctly.'
        assert (snpobj['variants_ref'][indexes] == alt_aux).all(),\
        'The reference and the alternate were not swapped correctly.'
        
        # Change 0's by 1's and 1's by 0's
        snps = snpobj['calldata_gt'][indexes,:,:]
        snpobj['calldata_gt'][indexes,:,:] = np.where((snps==0)|(snps==1), snps^1, snps)
        
        # Ensure the 0's and 1's where correctly swapped
        # Check that the number of 1's before the swap is the same as the number of 0's after the swap
        number_ones_before = np.sum(snps == 1)
        number_zeros_after = np.sum(snpobj['calldata_gt'][indexes,:,:] == 0)
        assert number_ones_before == number_zeros_after, 'An error occured while '\
        'swapping the zeros and ones.'
    
    return snpobj


def _get_chromosome_number(chrom_string):
    """
    Extracts the chromosome number from the given chromosome string.
    
    Parameters
    ----------
    chrom_string : str
        The chromosome identifier.
    
    Returns
    ------- 
    int or str
        If a valid chromosome number is found, returns the integer representation.
        If the chromosome string is 'X' or 'chrX', returns 10001.
        If the chromosome string is 'Y' or 'chrY', returns 10002.
        If the chromosome string is not standard, logs a warning and returns the original string.
    """
    if chrom_string.isdigit():
        return int(chrom_string)
    else:
        chrom_num = re.search(r'\d+', chrom_string)
        if chrom_num:
            return int(chrom_num.group())
        elif chrom_string.lower() in ['x', 'chrx']:
            return 10001
        elif chrom_string.lower() in ['y', 'chry']:
            return 10002
        else:
            log.warning(f"Chromosome nomenclature not standard. Chromosome: {chrom_string}")
            return chrom_string
