"""
Given a string columnTitle that represents the column title 
as appears in an Excel sheet, return its corresponding column number.

Example:
A -> 1
B -> 2
...
Z -> 26
AA -> 27
AB -> 28
...
ZY -> 701
etc
"""

class Solution:

    def columnToNumber(self, columnTitle: str) -> int:
        
        # Create a dictionary -> {'A': 1, 'B': 2,  ..., 'Z': 26}
        abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dic = {abc[i]:i+1 for i in range(len(abc))}
        
        # Input string to upper case
        columnTitle.upper()

        result = 0

        for letter in columnTitle:
            result = result*26 + dic[letter] 

        return result


if __name__ == "__main__":
    
    columnTitle = "XFD" 

    s = Solution().columnToNumber(columnTitle)

    print(s)
