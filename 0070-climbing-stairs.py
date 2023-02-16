import unittest


class Solution:
    def __init__(self):
        self.dictionary = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        if n in self.dictionary:
            return self.dictionary[n]

        self.dictionary[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.dictionary[n]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.climbStairs(1),
            1
        )

    def test02(self):
        self.assertEqual(
            self.solution.climbStairs(2),
            2
        )

    def test03(self):
        self.assertEqual(
            self.solution.climbStairs(3),
            3
        )

    def test04(self):
        self.assertEqual(
            self.solution.climbStairs(4),
            5
        )


if __name__ == '__main__':
    unittest.main()
