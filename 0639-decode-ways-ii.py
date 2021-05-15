import unittest
'''
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
'''


class Solution:

    def __init__(self):
        self.n = 10**9 + 7
        self.dictionary = dict()
        self.dictionary['*'] = 9
        for s in map(lambda i: f'{i}', range(1, 10)):
            self.dictionary[s] = 1

        self.dictionary['**'] = 15
        self.dictionary['1*'] = 9
        self.dictionary['2*'] = 6
        for s in map(lambda i: f'*{i}', range(0, 7)):
            self.dictionary[s] = 2
        for s in map(lambda i: f'*{i}', range(7, 10)):
            self.dictionary[s] = 1
        for s in map(lambda i: f'1{i}', range(0, 10)):
            self.dictionary[s] = 1
        for s in map(lambda i: f'2{i}', range(0, 7)):
            self.dictionary[s] = 1

    def numDecodings(self, s: str) -> int:
        self.mem = dict()
        self.s = s
        return self.dp(0)

    def dp(self, start: int) -> int:
        if start in self.mem:
            return self.mem[start]

        length = len(self.s) - start
        if length < 1:
            return 1

        one_char = self.s[start]
        if one_char in self.dictionary:
            case1 = self.dictionary[one_char] * self.dp(start + 1)
        else:
            case1 = 0

        if length < 2:
            self.mem[start] = case1
            return self.mem[start]

        two_char = self.s[start:start+2]
        if two_char in self.dictionary:
            case2 = self.dictionary[two_char] * self.dp(start + 2)
        else:
            case2 = 0

        self.mem[start] = (case1 + case2) % self.n
        return self.mem[start]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.numDecodings('*'),
            9
        )

    def test02(self):
        self.assertEqual(
            self.solution.numDecodings('1*'),
            18
        )

    def test03(self):
        self.assertEqual(
            self.solution.numDecodings('2*'),
            15
        )

    def test04(self):
        self.assertEqual(
            self.solution.numDecodings('111'),
            3
        )

    def test05(self):
        self.assertEqual(
            self.solution.numDecodings('1111'),
            5
        )

    def test06(self):
        self.assertEqual(
            self.solution.numDecodings('**'),
            96
        )

    def test07(self):
        self.assertEqual(
            self.solution.numDecodings("*********"),
            291868912
        )

    def test08(self):
        self.assertEqual(
            self.solution.numDecodings('0***********'),
            0
        )

    def test09(self):
        self.assertEqual(
            self.solution.numDecodings('***'),
            999
        )

    def test10(self):
        self.assertEqual(
            self.solution.numDecodings('****'),
            10431
        )


if __name__ == '__main__':
    unittest.main()
