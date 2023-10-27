"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

"""

def sortColors(nums: list[int]) -> None:

    ht = {0:0, 1:0, 2:0}

    for i in nums:
        ht[i] += 1

    j = 0
    k = 0

    for j in range(3):
        nums[k:ht[j] + k] = [j]*ht[j]
        k += ht[j]
    

#print(sortColors([0,1,1,2,1,0]))
