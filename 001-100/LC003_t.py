"""

Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Create a set for substring characters
        Initialize the longestSubstring at 0
        
        left and right indexes to delimitate the substring in main string

        Start with index left at 0, iterate moving the second index right

            If the character is not in the substring, added and update the longestSustring number
            Else remove the left chararter and move the left index one position

            Continue with this approach

        """
        n = len(s)
        longestSubstring = 0
        substringSet = set()
        
        left = 0
        
        for right in range(n):
            if s[right] not in substringSet:
                substringSet.add(s[right])
                longestSubstring = max(longestSubstring, right - left + 1)
            else:
                while s[right] in substringSet:
                    substringSet.remove(s[left])
                    left += 1
                substringSet.add(s[right])
        
        return longestSubstring