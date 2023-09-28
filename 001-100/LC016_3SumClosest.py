"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

import itertools

def threeSumClosest(nums: list[int], target: int) -> int:
    """
    Create all triplets in the array and calculate the sum of the three elements.
    Calculate the distance between that sum and the target
    """

    #inicialize the sum of the first triplet
    result = nums[0] + nums[1] + nums[2]
    # inicialize the min_distance
    min_distance = abs(result - target)

    for i, j, k in itertools.combinations(nums, 3):
        if abs(i + j + k - target) <= min_distance:
            result = i + j + k 
            min_distance = abs(result - target)

    return result

#print(threeSumClosest(nums = [-1,2,1,-4], target=1))