"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example: 
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]


if __name__ == "__main__":
    
    arr = [1, 2, 3, 4, 5, 6, 7]

    Solution().rotate(nums=arr, k=3)
    
    print(arr)
