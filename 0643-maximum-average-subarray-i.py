import unittest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Find a contiguous subarray whose length is equal to k that has the
        maximum average value and return this value.

        Time complexity: O(n)
        Space complexity: O(1)
        '''
        sum_subarray = sum(nums[:k])
        max_sum_subarray = sum_subarray
        for i in range(len(nums) - k):
            sum_subarray += nums[k+i] - nums[i]
            if sum_subarray > max_sum_subarray:
                max_sum_subarray = sum_subarray
        return max_sum_subarray / k


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.findMaxAverage(
                [5], 1
            ),
            5
        )

    def test02(self):
        self.assertEqual(
            self.solution.findMaxAverage(
                [0, 5, 3, 2, 1, 0], 1
            ),
            5
        )

    def test03(self):
        self.assertEqual(
            self.solution.findMaxAverage(
                [0, 4, 0, 3, 2], 1
            ),
            4
        )


if __name__ == '__main__':
    unittest.main()
