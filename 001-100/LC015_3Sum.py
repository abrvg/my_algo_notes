"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    
    """
    Create all the triplets in the list. 
    For each triplet, compare if the sum of the triplet elements is zero
        if yes, add to the result list (in case they are not part)
    """

    n = len(nums)
    
    result = []

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):

                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])

                    if triplet not in result:
                        result.append(triplet)

    return result





# A More Pythonic solution, using itertools
import itertools

def threeSumPythonic(nums: list[int]) -> list[list[int]]:
    
    result =[]
    
    for i, j, k in itertools.combinations(nums, 3):
        if i + j + k == 0:
            triplet = sorted([i,j,k])
            
            if triplet not in result:
                result.append(triplet)
    
    return result



