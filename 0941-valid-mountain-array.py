from typing import List
import unittest


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        left_peek = -1
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                left_peek = i
            else:
                break

        right_peek = len(arr)
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                right_peek = i
            else:
                break

        # print(left_peek, right_peek)
        return left_peek == right_peek


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.validMountainArray([0, 1, 2]),
            False
        )

    def test02(self):
        self.assertEqual(
            self.solution.validMountainArray([0, 1, 2, 1, 4]),
            False
        )

    def test03(self):
        self.assertEqual(
            self.solution.validMountainArray([2, 1]),
            False
        )

    def test04(self):
        self.assertEqual(
            self.solution.validMountainArray([3, 5, 5]),
            False
        )

    def test05(self):
        self.assertEqual(
            self.solution.validMountainArray([4, 5, 9, 1]),
            True
        )

    def test06(self):
        self.assertEqual(
            self.solution.validMountainArray([9, 6, 3, 2]),
            False
        )

    def test07(self):
        self.assertEqual(
            self.solution.validMountainArray([1, 2, 5, 12]),
            False
        )


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
