import unittest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        Use the two pointer method
        Time complexity: O(n^2)
        '''
        if len(nums) < 3:
            raise Exception('length of nums must be longer than or equal to 3')

        nums.sort()
        closest_diff = nums[0] + nums[1] + nums[-1] - target

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                diff = nums[i] + nums[left] + nums[right] - target
                if diff == 0:
                    return target
                if abs(diff) < abs(closest_diff):
                    closest_diff = diff
                if diff < 0:
                    left += 1
                else:  # diff > 0
                    right -= 1

        return target + closest_diff


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [-1, 2, 1, -4],
                1
            ),
            2
        )

    def test02(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [-1, 2, 1, -4],
                2
            ),
            2
        )

    def test03(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [0, 0, 0],
                100
            ),
            0
        )

    def test04(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1],
                1
            ),
            1
        )

    def test05(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [1, 2, -2, -1],
                6
            ),
            2
        )

    def test06(self):
        self.assertEqual(
            self.solution.threeSumClosest(
                [1, 2, -2, -1],
                -10
            ),
            -2
        )


if __name__ == '__main__':
    unittest.main()
