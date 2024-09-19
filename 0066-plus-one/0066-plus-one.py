class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum_num = 0
        len_digits = len(digits)
        for i, digit in enumerate(digits):
            sum_num += digit * (10**(len_digits - i - 1))
        sum_num = sum_num + 1 
        output = [int(i) for i in str(sum_num)]
        return output