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

def groupAnagrams(strs):

    # create a hash table to store anagram group
    # hash table will be a key for sorted string and the value is the list of string that belongs to this group
    angrm_groups = {}

    # Iterate over the array, sort the string as a key and look
    #for the corresponding anagram group in hastable
    for string in strs:
        sorted_str = ''.join(sorted(string))

    #If anagram doesn't exist, create a new anagram group
    # Otherwise , add the string to the extisting group
        if sorted_str not in angrm_groups:
            angrm_groups[sorted_str] = []
        
        angrm_groups[sorted_str].append(string)

    # Return the values of the hash table
    return list(angrm_groups.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))