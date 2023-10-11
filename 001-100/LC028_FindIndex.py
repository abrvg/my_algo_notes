"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

def strStr(haystack:str, needle:str) -> int:
    n = len(haystack)
    m = len(needle)
    
    index = 0

    while 0 <= index <= (n-m):
        if haystack[index:index+m] == needle:
            return index
            break
        index += 1

    return -1

        