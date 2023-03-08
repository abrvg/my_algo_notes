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
        Check if the element resulting from difference of target and actual element exists in the hastable
            If true, return the actual index element and the index of the difference from the hastable
        Insert the actual element into the hashtable with its associated index
        """
        dic = {}

        for i in range(len(arr)):
            var = arr[i]

            if target - var in dic:
                return [dic[target-var], i]
            
            dic[var] = i


if __name__ == "__main__":
    
    arr = [3, 7, 18, 1, 8, 95, 4]
    target = 19

    s = Solution().twoSum(arr, target)

    print(s)