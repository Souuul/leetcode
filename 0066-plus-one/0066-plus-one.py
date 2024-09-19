class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_num = ''
        output_num = 0
        output = []
        for i in digits:
            string_num += str(i)
        output_num = str(int(string_num) + 1)

        for k in output_num:
            output.append(int(k))
        return output