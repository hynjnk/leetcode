import re
import unittest


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = f"^{p}$"  # match exactly
        result = re.search(p, s)
        print(f"pattern: {p}, string: {s}, result: {result}")
        if (result):
            return True
        else:
            return False


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        s = "aa"
        p = "a"
        expected = False
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test02(self):
        s = "aa"
        p = "a*"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test03(self):
        s = "ab"
        p = ".*"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test04(self):
        s = "aab"
        p = "c*a*b"
        expected = True
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test05(self):
        s = "mississippi"
        p = "mis*is*p*."
        expected = False
        self.assertEqual(self.solution.isMatch(s, p), expected)

    def test06(self):
        s = "mississippi"
        p = "."
        expected = False
        self.assertEqual(self.solution.isMatch(s, p), expected)


if __name__ == "__main__":
    unittest.main()
