class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_string = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if digits == '':
            return []
        groups = [number_string[digit] for digit in digits]
        combinations = [''.join(combo) for combo in product(*groups)]
        return combinations