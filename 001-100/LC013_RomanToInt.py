"""
Given a string that represent a roman number, convert it to integer
"""

def romanToInt(self, s: str) -> int:
    num_map = {
        "I": 1, "V": 5, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    num = 0

    # Made replacements
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    # Now just add the char based on the hash table
    for char in s:
        num += num_map[char]
    
    return num


# Alternative solution without replacements
# substarcting the number at left side
def romanToIntAlt(self, s: str) -> int:
    num_map = {
        "I": 1, "V": 5, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    num = 0

    for i in range(len(s)):
        
        if i < len(s) - 1 and num_map[s[i]] < num_map[s[i+1]]:
            num -= num_map[s[i]]

        else: 
            num += num_map[s[i]]

    return num
