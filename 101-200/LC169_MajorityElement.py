"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter_dict = {}
        n = len(nums)
        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 0

            counter_dict[num] += 1

            if counter_dict[num] > n // 2:
                return num


    def majorityElementBMA(self, nums: List[int]) -> int:
        """
        Using the Boyer - Moore Voting Algorithm
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate
