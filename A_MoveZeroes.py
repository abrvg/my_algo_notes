"""
Given an array of integers, move all the zeroes to the end and maintain the 
relative order of the non-zero elements
Example
input -> arr = [5, 1, 0, 8, 0, 6]
output -> [5, 1, 8, 6, 0, 0]

"""

class Solution:
    
    def moveZero(self, arr):

        i = 0
        j = 0

        while j < len(arr):
            if arr[j] == 0:
                j += 1
            else:
                arr[i] = arr[j]
                i += 1
                j += 1

        while i < len(arr):
            arr[i] = 0
            i += 1
        
        return arr


if __name__ == "__main__":
    
    arr = [3, 7, 0, 1, 8, 0, 4]

    s = Solution().moveZero(arr)

    print(s)