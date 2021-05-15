import unittest
'''
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
'''


class Solution:

    def __init__(self):
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
        # https://leetcode.com/problems/decode-ways-ii/discuss/105262/Python-6-lines-DP-solution
        prev = 1
        cur = self.dictionary.get(s[0], 0)
        for i in range(1, len(s)):
            case0 = self.dictionary.get(s[i-1:i+1], 0) * prev
            case1 = self.dictionary.get(s[i], 0) * cur

            prev = cur
            cur = (case0 + case1) % 1000000007
        return cur


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
