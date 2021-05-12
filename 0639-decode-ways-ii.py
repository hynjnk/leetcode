import unittest
import re
'''
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
'''


class Solution:
    n = 10**9 + 7
    mem = {"": 1}

    def numDecodings(self, s: str) -> int:
        if s in self.mem:
            return self.mem[s]
        length = len(s)
        if length == 1:
            result = self.numDecodings1Char(s)
            self.mem[s] = result
            return result
        else:
            # Case 1: Devide 3 piece 'a..b' + 'cd' + 'e...f'
            case1 = self.numdecodings2Char(s[length//2-1:length//2+1])
            if case1 > 0:
                case1 *= self.numDecodings(s[:length//2-1])
            if case1 > 0:
                case1 *= self.numDecodings(s[length//2+1:])

            # Case 2: Devide 2 piece 'a..bc' + 'de...f'
            case2 = self.numDecodings(s[:length//2])
            if case2 > 0:
                case2 *= self.numDecodings(s[length//2:])
            result = (case1 + case2) % self.n
            self.mem[s] = result
            return result

    def numDecodings1Char(self, s: str) -> int:
        if s == '*':
            return 9
        if re.search(r'^[1-9]$', s):
            return 1
        return 0

    def numdecodings2Char(self, s: str) -> int:
        if s == '**':  # 11~19, 21~26
            return 15
        if re.search(r'^\*[0-6]$', s):
            return 2
        if re.search(r'^\*[7-9]$', s):
            return 1
        if s == '1*':
            return 9
        if s == '2*':
            return 6
        if re.search(r'^1[0-9]$', s):
            return 1
        if re.search(r'^2[0-6]$', s):
            return 1
        return 0


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

if __name__ == '__main__':
    unittest.main()
