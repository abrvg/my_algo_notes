"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        k -= 1
        factorial = [1]
        for i in range(1,n):
            factorial.append(factorial[-1]*i)

        result = []
        for i in range(n-1, 0, -1):
            index = k//factorial[i]
            result.append(nums[index])
            del nums[index]
            k %= factorial[i]

        result.append(nums[0])

        return ''.join(map(str, result))
        
