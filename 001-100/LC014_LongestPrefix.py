"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        1.- Sort the array (alphabetically) 
        2.- Compare first and last elements, char by char
            If they match, add to the prefix output
        3.- Determine the longest prefix


        """

        strs.sort()

        first_word = strs[0]
        last_word = strs[-1]

        n = len(first_word)
        m = len(last_word)

        prefix = ''

        for i in range(min(n,m)):
            if first_word[i] == last_word[i]:
                prefix += first_word[i]
            else:
                break

        return prefix
