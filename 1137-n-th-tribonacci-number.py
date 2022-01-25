import unittest


class Solution:
    def __init__(self) -> None:
        self.dictionary = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.dictionary:
            return self.dictionary[n]

        self.dictionary[n] = self.tribonacci(n-3)
        self.dictionary[n] += self.tribonacci(n-2)
        self.dictionary[n] += self.tribonacci(n-1)
        return self.dictionary[n]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.tribonacci(0),
            0
        )

    def test02(self):
        self.assertEqual(
            self.solution.tribonacci(1),
            1
        )

    def test03(self):
        self.assertEqual(
            self.solution.tribonacci(2),
            1
        )

    def test04(self):
        self.assertEqual(
            self.solution.tribonacci(3),
            2
        )

    def test05(self):
        self.assertEqual(
            self.solution.tribonacci(4),
            4
        )

    def test06(self):
        self.assertEqual(
            self.solution.tribonacci(5),
            7
        )


if __name__ == '__main__':
    unittest.main()
