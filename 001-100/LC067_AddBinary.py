"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        carry = 0

        for i in range(max_len - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry

            if bit_sum == 0:
                result = "0" + result 
                carry = 0

            elif bit_sum == 1:
                result = "1" + result 
                carry = 0

            elif bit_sum == 3:
                result = "1" + result
                carry = 1

            else:
                result = "0" + result 
                carry = 1
            
        if carry:
            result = "1" + result

        return result
