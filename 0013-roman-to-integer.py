import unittest
import re

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''


class Solution:
    patterns = [
        'M', 'CM', 'D', 'CD',
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]

    def romanToInt(self, s: str) -> int:
        s_i = 0
        p_i = 0
        result = 0

        while p_i < len(self.patterns):
            # print(f"\nre.match({self.patterns[p_i]}, {s[s_i:]}) ", end="")
            while re.match(self.patterns[p_i], s[s_i:]):
                # print("x", end="")
                result += self.values[p_i]
                s_i += len(self.patterns[p_i])
            p_i += 1
        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        expected = 3
        s = 'III'
        self.assertEqual(self.solution.romanToInt(s), expected)

    def test02(self):
        expected = 4
        s = 'IV'
        self.assertEqual(self.solution.romanToInt(s), expected)

    def test03(self):
        expected = 9
        s = 'IX'
        self.assertEqual(self.solution.romanToInt(s), expected)

    def test04(self):
        expected = 58
        s = 'LVIII'
        self.assertEqual(self.solution.romanToInt(s), expected)

    def test05(self):
        expected = 1994
        s = 'MCMXCIV'
        self.assertEqual(self.solution.romanToInt(s), expected)


if __name__ == "__main__":
    unittest.main()
