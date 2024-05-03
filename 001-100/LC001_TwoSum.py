"""
Given an array of integers, return indices of the two elements such that
they add up to a specific target

Example:
A = [4, 5, 7, 1], target = 6
Output -> [1, 3]

Explanation: A[1] + A[3] = 6
"""

class Solution:
    def twoSum(self, arr, target):
        """
        Create a hash table with no elements
        Traverse the elements of the array
        Check if the element resulting from difference of target and actual element exists in the hashtable
            If true, return the actual index element and the index of the difference from the hashtable
        Insert the actual element into the hashtable with its associated index
        """
        
        hash_table = {}
        
        for i, num in enumerate(nums):
            complement = target - num

            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[num] = i

        return []
