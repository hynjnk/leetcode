import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea, self.area(left, right, height))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

    def area(self, left: int, right: int, height: List[int]) -> int:
        return min(height[left], height[right]) * (right - left)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        height = [1, 1]
        expected = 1
        self.assertEqual(self.solution.maxArea(height), expected)

    def test02(self):
        height = [4, 3, 2, 1, 4]
        expected = 16
        self.assertEqual(self.solution.maxArea(height), expected)

    def test03(self):
        height = [1, 2, 1]
        expected = 2
        self.assertEqual(self.solution.maxArea(height), expected)

    def test04(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(self.solution.maxArea(height), expected)


if __name__ == "__main__":
    unittest.main()
