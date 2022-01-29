from typing import List
import unittest


class Solution:
    def jump(self, nums: List[int]) -> int:
        # O(N) Time
        # O(1) Space

        if len(nums) == 1:
            return 0  # No need to jump

        count = 0
        max_jump_index = 0
        max_next_jump_index = 0
        for i in range(0, len(nums)):
            max_next_jump_index = max(max_next_jump_index, i + nums[i])
            if i > max_jump_index:
                return -1  # Can't not jump to goal
            if i == max_jump_index:
                count += 1  # Jump
                max_jump_index = max_next_jump_index
                if max_jump_index >= len(nums)-1:
                    return count  # No need to check remains

        return -1


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.jump(
                [2, 3, 1, 1, 4]),
            2
        )

    def test02(self):
        self.assertEqual(
            self.solution.jump(
                [2, 3, 0, 1, 4]),
            2
        )

    def test03(self):
        self.assertEqual(
            self.solution.jump(
                [6, 1, 3, 2, 3, 0]),
            1
        )

    def test04(self):
        self.assertEqual(
            self.solution.jump(
                [0]),
            0
        )

    def test05(self):
        self.assertEqual(
            self.solution.jump(
                [
                    7, 0, 0, 0, 0, 0,
                    5, 0, 0, 0,
                    5, 0, 0, 0,
                    5, 0, 0, 0,
                    5, 0, 0, 0,
                ]),
            5
        )

    def test06(self):
        self.assertEqual(
            self.solution.jump(
                [3, 2, 1, 0, 4]),
            -1
        )

    def test07(self):
        self.assertEqual(
            self.solution.jump(
                [3, 2, 1, 1, 0]),
            2
        )

    def test08(self):
        self.assertEqual(
            self.solution.jump(
                [0, 0, 4]),
            -1
        )


if __name__ == '__main__':
    unittest.main()
