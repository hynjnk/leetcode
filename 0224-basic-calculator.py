from collections import namedtuple
import unittest


class Solution:
    def calculate(self, s: str) -> int:
        self.s = s
        result, _, _ = self.calc(0)
        return result

    def read_term(self, start: int):
        value = None
        for i in range(start, len(self.s)):
            c = self.s[i]
            if c == ' ':
                continue
            elif c == '(':
                return self.calc(i + 1)
            elif c == ')':
                if value is None:
                    raise ValueError('invalid expression')
                else:
                    return value, i+1, c
            elif c == '-':
                if value is None:
                    positive_term, next, op = self.read_term(i + 1)
                    return -positive_term, next, op
                else:
                    return value, i+1, c
            elif c == '+':
                if value is None:
                    raise ValueError('invalid expression')
                else:
                    return value, i+1, c
            elif '0' <= c and c <= '9':
                if value is None:
                    value = int(c)
                else:
                    value = value * 10 + int(c)
            else:
                raise ValueError('invalid expression')
        return value, len(self.s), "end"

    def calc(self, start: int) -> tuple[int]:
        left, next, op = self.read_term(start)
        while next < len(self.s) and op != ')':
            right, next, next_op = self.read_term(next)
            if op == '+':
                left += right
            elif op == '-':
                left -= right
            op = next_op

        if next >= len(self.s):
            return left, next, op

        if next < len(self.s) and op == ')':
            while next < len(self.s) and self.s[next] == ' ':
                next += 1
            if next < len(self.s):
                if self.s[next] == ')':
                    next += 1
                    op = ')'
                elif self.s[next] == '+':
                    next += 1
                    op = '+'
                elif self.s[next] == '-':
                    next += 1
                    op = '-'
                else:
                    raise ValueError('invalid expression')

        return left, next, op


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        s = "  123  "
        expected = 123
        self.assertEqual(self.solution.calculate(s), expected)

    def test02(self):
        s = "  123 + 1"
        expected = 124
        self.assertEqual(self.solution.calculate(s), expected)

    def test03(self):
        s = "12-13"
        expected = -1
        self.assertEqual(self.solution.calculate(s), expected)

    def test04(self):
        s = " -123"
        expected = -123
        self.assertEqual(self.solution.calculate(s), expected)

    def test05(self):
        s = "1+ 1 + 3"
        expected = 5
        self.assertEqual(self.solution.calculate(s), expected)

    def test06(self):
        s = "1 - 1 + 3"
        expected = 3
        self.assertEqual(self.solution.calculate(s), expected)

    def test07(self):
        s = "1 - (1 + 3)"
        expected = -3
        self.assertEqual(self.solution.calculate(s), expected)

    def test08(self):
        s = "-(3 + (4 + 5))"
        expected = -12
        self.assertEqual(self.solution.calculate(s), expected)

    def test09(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        self.assertEqual(self.solution.calculate(s), expected)


if __name__ == "__main__":
    unittest.main()
