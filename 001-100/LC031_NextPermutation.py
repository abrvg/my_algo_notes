"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

"""

def nextPermutation(nums: list[int]) -> None:
    
    #print(nums)
    
    n = len(nums)
    i = n-2

    if n > 1:
        # Iterate over the array from right to left
        # Find the index where the order breaks (nums[i]<nums[i+1])
        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1

        # If the index does not exist, it's the last permutation, so just reverse the list
        if i < 0:
            nums[:] = nums[::-1]
        else:
            # Find the smallest index j greater than i such that nums[j] > nums[i]
            j = i+1
            while j < n and nums[j] > nums[i]:
                j += 1

            # and swap nums[i] and nums[j]
            nums[i], nums[j-1] = nums[j-1], nums[i]
            # Reverse the subarray nums[i+1:]
            nums[i+1:] = nums[i+1:][::-1]

    #print(nums)
    #print()




# nextPermutation([5,5,3,2,1])
# nextPermutation([5,4,3,2,1])
# nextPermutation([1,4,3,5,2])
# nextPermutation([2,3,1])
# nextPermutation([1,3,2])
# nextPermutation([2,2])
# nextPermutation([])