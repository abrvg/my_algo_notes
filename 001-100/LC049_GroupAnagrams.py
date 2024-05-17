"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

"""

def groupAnagrams(strs: List[str]):

    # create a hash table to store anagram group
    # hash table will be a key for sorted string and the value is the list of string that belongs to this group
    anagrams = {}

    # Iterate over the array, sort the string as a key 
    for string in strs:
        #If anagram doesn't exist, create a new anagram group
        # Otherwise , add the string to the extisting group
        sorted_string = '.join(sorted(string))
        anagrams.setdefault(sorted_string,[]).append(string)

    # Return the values of the hash table
    return list(anagrams.values())
