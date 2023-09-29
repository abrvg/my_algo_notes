"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that 
the number could represent. Return the answer in any order.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]

"""

def combine_two_arrays(arr1: list[str], arr2: list[str]):

    """
    Given two arrays, combine the string elements from the first array with the elements of the second array

    Args: 
        arr1 and arr2: A list of strings
    Returns:
        List of combination of string from arr1 and arr1
    
    >>> combine_two_arrays([], [])
    []

    >>> combine_two_arrays([], ["b"])
    ["b"]

    >>> combine_two_arrays(["a", "b"], ["c"])
    ["ac", "bc"]

    >>> combine_two_arrays(["a","b"], ["c", "d"])
    ["ac", "ad", "bc", "bd"]
    """
    

    result = []

    # Case, non empty arrays can be combined in a loop
    if len(arr1) != 0 and len(arr2) != 0:
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                result.append(arr1[i] + arr2[j])
    
    # If at least one array is empty, jus merge with the other (no need to combine)
    else:
        result = arr1 + arr2 

    return result 






def letterCombinations(digits: str) -> list[str]:

    # Create a hash table to relate the digits with the letters (phone digits to letter)
    num_to_dig = {"0":[], "1":[], "2": ["a", "b", "c"], "3": ["d", "e", "f"], 
                  "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], 
                  "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], 
                  "9" :["w", "x", "y", "z"]
                 }
    
    # initialize the output array
    arr_out = []
    
    for num_char in digits:

        # Get the letter array asociated with every number in the hash table
        arr2 = num_to_dig.get(num_char)

        # Combine the previous array with the one for the  output
        arr_out = combine_two_arrays(arr_out, arr2)
        
    return arr_out
