"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, number: int) -> int:
        # Detailed answer, using only numbers

        rebmun = 0

        if number > 2**31 + 1 or number < -2**31:
            pass
        
        else:           
            number = abs(number)
            last = 0

            while number > 0:
                # Compute the last digit of the number
                last = number - int(number/10)*10
                
                # Multiply by 10 and add the last digit in the answer
                rebmun = rebmun*10 + last 
                
                # remove the last digit in the original number
                number = int(number/10)
          
        return rebmun * (1 if number >= 0 else -1)
    
    
    
    def reverse_py(self, number: int) -> int:
        # Pythonic solution, cast the number to string, reverse string
        # cast against to integer, multiply by the sign
        rebnum = int(str(abs(number))[::-1]) * (1 if number >= 0 else -1)
        return rebnum if -2**31 <= rebnum < 2**31 else 0



if __name__ == "__main__":

    number = -98745
    
    sol = Solution().reverse(number)
    print(sol)

    sol_py = Solution().reverse_py(number)
    print(sol_py)  
