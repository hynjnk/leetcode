import unittest


class Solution00:
    brackets_open = {"(": 0, "{": 1, "[": 2}
    brackets_close = {")": 0, "}": 1, "]": 2}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.brackets_open:
                stack.append(self.brackets_open[c])
            elif c in self.brackets_close:
                if not stack or stack.pop() != self.brackets_close[c]:
                    return False
            else:
                return False

        return len(stack) == 0


class Solution:
    brackets = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.brackets:
                stack.append(c)
            elif len(stack) == 0 or self.brackets[stack.pop()] != c:
                return False

        return len(stack) == 0


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.isValid("()"),
            True
        )

    def test02(self):
        self.assertEqual(
            self.solution.isValid("()[]{}"),
            True
        )

    def test03(self):
        self.assertEqual(
            self.solution.isValid("(]"),
            False
        )

    def test04(self):
        self.assertEqual(
            self.solution.isValid("([)]"),
            False
        )

    def test05(self):
        self.assertEqual(
            self.solution.isValid("([])"),
            True
        )

    def test06(self):
        self.assertEqual(
            self.solution.isValid(")"),
            False
        )


if __name__ == '__main__':
    unittest.main()
