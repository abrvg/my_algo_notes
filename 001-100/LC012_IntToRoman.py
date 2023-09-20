"""
Given an integer, convert it to a roman numeral.
"""

def intToRoman(self, num: int) -> str:
    num_map = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 
        10: "X", 40:"XL", 50: "L", 90: "XC", 
        100: "C", 400: "CD", 500: "D", 900: "CM", 
        1000: "M"}

    if num < 1 or num >1000:
        return "Out of range"
    
    else:
        var = ''
        for i in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while i <= num:
                var += num_map[i]
                num -= i
        return var
