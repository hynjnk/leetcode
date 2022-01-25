import unittest


class Solution:
    def __init__(self) -> None:
        self.dictionary = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n in self.dictionary:
            return self.dictionary[n]

        self.dictionary[n] = self.fib(n-2) + self.fib(n-1)
        return self.dictionary[n]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.fib(83),
            99194853094755497
        )

    def test02(self):
        self.assertEqual(
            self.solution.fib(0),
            0
        )

    def test03(self):
        self.assertEqual(
            self.solution.fib(1),
            1
        )

    def test04(self):
        self.assertEqual(
            self.solution.fib(2),
            1
        )

    def test05(self):
        self.assertEqual(
            self.solution.fib(3),
            2
        )

    def test06(self):
        self.assertEqual(
            self.solution.fib(4),
            3
        )


if __name__ == '__main__':
    unittest.main()
