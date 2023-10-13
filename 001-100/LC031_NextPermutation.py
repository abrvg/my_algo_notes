"""
Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

"""

def nextPermutation(nums: list[int]) -> None:
    
    print(nums)
    i = 1
    n = len(nums)

    #
    if n > 1:
        # Find the index where the order breaks, strating from the extreme right in the list
        while (nums[-i] <= nums[-i -1]) and (i < n-1)  :
            i += 1

        #If the index is found at the begining of the list and the order is preserved, 
        # the order should be broken in the element at position -1 
        if i+1 == n and nums[-i] <= nums [-i-1]:
            k = 1
        else: 
            k = i + 1
    

        # Find the index where the max element is located  in the remaining list
        max_slice_ele = nums[-1]
        m = -1
        for l in range(-i-1,0):
            if nums[l] > max_slice_ele:
                max_slice_ele = nums[l]
                m = l

        # swap the elements where the order breaks and the max element in the remaining
        nums[-k], nums[m] = nums[m], nums[-k]

        # after swaping, order the remaing indexes
        nums[:] = nums[:-i] + sorted(nums[-i:])

        print(nums)
        print()
    





#nextPermutation([5,5,3,2,1])
#nextPermutation([5,4,3,2,1])
#nextPermutation([1,4,3,5,2])
#nextPermutation([2,3,1])
nextPermutation([1,3,2])
#nextPermutation([2,2])
#nextPermutation([])