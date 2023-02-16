from typing import List
import unittest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0

        one_step_ahead_cost = 0
        two_step_ahead_cost = 0
        for i in range(len(cost)-2, -1, -1):
            temp = min(
                cost[i] + one_step_ahead_cost,
                cost[i+1] + two_step_ahead_cost
            )
            two_step_ahead_cost = one_step_ahead_cost
            one_step_ahead_cost = temp

        return one_step_ahead_cost


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.minCostClimbingStairs([10, 15, 20]),
            15
        )

    def test02(self):
        self.assertEqual(
            self.solution.minCostClimbingStairs(
                [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
            6
        )


if __name__ == '__main__':
    unittest.main()
