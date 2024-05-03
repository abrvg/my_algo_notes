"""
Given an integer x, return true if x is palindrome

Example 1
input: x=121
output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

class Solution:
    
    #def __init__(self, x):
    #    self.x = x
    
    def isPalindrome(self,x):
        self.x = x
        return str(self.x) == str(self.x)[::-1]


    def isPalindromeII(self, x: int) -> bool:
        stringx = str(x)

        for i in range(len(stringx)//2):
            if stringx[i] != stringx[-1-i]:
                return False

        return True

x = 10
s = Solution().isPalindrome(x)
print(s)
