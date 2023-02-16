from typing import List
import unittest


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # O(N) Time
        # O(1) Space

        minimum_to_jump = -1
        for i in range(len(nums)-1, -1, -1):
            minimum_to_jump += 1
            if nums[i] >= minimum_to_jump:
                minimum_to_jump = 0

        return minimum_to_jump <= 0


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.canJump(
                [2, 3, 1, 1, 4]),
            True
        )

    def test02(self):
        self.assertEqual(
            self.solution.canJump(
                [3, 2, 1, 0, 4]),
            False
        )

    def test03(self):
        self.assertEqual(
            self.solution.canJump(
                [0]),
            True
        )

    def test04(self):
        self.assertEqual(
            self.solution.canJump(
                [1, 0]),
            True
        )

    def test05(self):
        self.assertEqual(
            self.solution.canJump(
                [3, 0, 0]),
            True
        )

    def test06(self):
        self.assertEqual(
            self.solution.canJump(
                [4, 2, 1, 0, 4, 0]),
            True
        )

    def test07(self):
        self.assertEqual(
            self.solution.canJump(
                [1]),
            True
        )

    def test08(self):
        self.assertEqual(
            self.solution.canJump(
                [0, 1]),
            False
        )

    def test09(self):
        self.assertEqual(
            self.solution.canJump(
                [3, 0, 7, 0, 0, 0]),
            True
        )


if __name__ == '__main__':
    unittest.main()
