import unittest

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
    '''
    1 <= num <= 3999
    '''
    def intToRoman(self, num: int) -> str:
        # build units digit
        num, mod = divmod(num, 10)
        if mod < 4:
            roman = 'I' * mod
        elif mod == 4:
            roman = 'IV'
        elif mod < 9:
            roman = 'V' + 'I' * (mod-5)
        else:
            roman = 'IX'
        if num == 0:
            return roman

        # build tens digit
        num, mod = divmod(num, 10)
        if mod < 4:
            roman = 'X' * mod + roman
        elif mod == 4:
            roman = 'XL' + roman
        elif mod < 9:
            roman = 'L' + 'X' * (mod-5) + roman
        else:
            roman = 'XC' + roman
        if num == 0:
            return roman

        # build hundreds digit
        num, mod = divmod(num, 10)
        if mod < 4:
            roman = 'C' * mod + roman
        elif mod == 4:
            roman = 'CD' + roman
        elif mod < 9:
            roman = 'D' + 'C' * (mod-5) + roman
        else:
            roman = 'CM' + roman

        # build thousands digit
        num, mod = divmod(num, 10)
        return 'M' * mod + roman


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        num = 3
        expected = 'III'
        self.assertEqual(self.solution.intToRoman(num), expected)

    def test02(self):
        num = 4
        expected = 'IV'
        self.assertEqual(self.solution.intToRoman(num), expected)

    def test03(self):
        num = 9
        expected = 'IX'
        self.assertEqual(self.solution.intToRoman(num), expected)

    def test04(self):
        num = 58
        expected = 'LVIII'
        self.assertEqual(self.solution.intToRoman(num), expected)

    def test05(self):
        num = 1994
        expected = 'MCMXCIV'
        self.assertEqual(self.solution.intToRoman(num), expected)


if __name__ == "__main__":
    unittest.main()
