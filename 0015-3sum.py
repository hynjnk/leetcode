import unittest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            result += self.twoSum(nums[i+1:], nums[i])

        return result

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        return a list of [target, num1, num2],
        where target + num1 + num2 = 0 and
        num1 < num2, num1, num2 in sorted nums
        '''
        result = []
        left = 0
        right = len(nums) - 1
        while left < right:
            s = target + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                result.append([target, nums[left], nums[right]])
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
                while nums[right] == nums[right+1] and left < right:
                    right -= 1
        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        self.assertEqual(
            self.solution.threeSum(
                [-1, 0, 1, 2, -1, -4]
            ),
            [[-1, -1, 2], [-1, 0, 1]]
        )

    def test02(self):
        self.assertEqual(
            self.solution.threeSum(
                []
            ),
            []
        )

    def test03(self):
        self.assertEqual(
            self.solution.threeSum(
                [0]
            ),
            []
        )

    def test04(self):
        self.assertEqual(
            self.solution.threeSum(
                [1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1]
            ),
            [[-1, 0, 1], [0, 0, 0]]
        )

    def test05(self):
        self.assertEqual(
            self.solution.threeSum(
                [1, 2, -2, -1]
            ),
            []
        )


if __name__ == '__main__':
    unittest.main()
