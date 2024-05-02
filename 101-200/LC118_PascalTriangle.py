"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for n in range(1,numRows+1):
            row = []
            
            for k in range(n):
                row.append(math.comb(n-1,k))

            output.append(row)

        return output
