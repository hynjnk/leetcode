from typing import List
from itertools import product

DIGIT_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for d in digits:
            additional = list(DIGIT_TO_LETTERS[d])
            if result:
                result = list(map(
                    lambda t: ''.join(t),
                    product(result, additional)
                ))
            else:
                result = additional
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('2'))
    print(solution.letterCombinations('273'))
