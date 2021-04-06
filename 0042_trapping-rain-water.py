import unittest
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        self.height = height

        trapped = 0
        left = 0
        right = len(height) - 1
        height_left = height[left]
        height_right = height[right]
        while left < right:
            # print(f'left: {left}, right: {right}, height: {height[left:right+1]}, trapped: {trapped}')
            if height_left < height_right:
                left += 1
                if height[left] > height_left:
                    height_left = height[left]
                else:
                    trapped += height_left - height[left]
            else:
                right -= 1
                if height[right] > height_right:
                    height_right = height[right]
                else:
                    trapped += height_right - height[right]

        return trapped


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(self.solution.trap(height), expected)

    def test02(self):
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        self.assertEqual(self.solution.trap(height), expected)

    def test03(self):
        height = [1, 2, 1]
        expected = 0
        self.assertEqual(self.solution.trap(height), expected)

    def test04(self):
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 0 + 0 + 2 + 6 + 3 + 4 + 0 + 4 + 0
        self.assertEqual(self.solution.trap(height), expected)


if __name__ == "__main__":
    unittest.main()
