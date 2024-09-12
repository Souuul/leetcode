class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        convert_numbers = 0
        index = 0
        
        while index < len(s):
            if index + 1 < len(s) and roman_dict[s[index]] < roman_dict[s[index + 1]]:
                convert_numbers += roman_dict[s[index + 1]] - roman_dict[s[index]]
                index += 2
            else:
                convert_numbers += roman_dict[s[index]]
                index += 1
                
        return convert_numbers