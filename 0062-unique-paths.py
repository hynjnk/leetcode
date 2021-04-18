import math
import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = math.factorial(m + n - 2)
        result //= math.factorial(m - 1)
        result //= math.factorial(n - 1)
        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        m = 3
        n = 7
        expected = 28
        self.assertEqual(self.solution.uniquePaths(m, n), expected)

    def test02(self):
        m = 3
        n = 2
        expected = 3
        self.assertEqual(self.solution.uniquePaths(m, n), expected)

    def test03(self):
        m = 7
        n = 3
        expected = 28
        self.assertEqual(self.solution.uniquePaths(m, n), expected)

    def test04(self):
        m = 3
        n = 3
        expected = 6
        self.assertEqual(self.solution.uniquePaths(m, n), expected)


if __name__ == "__main__":
    unittest.main()
