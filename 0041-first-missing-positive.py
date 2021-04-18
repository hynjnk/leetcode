import unittest
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return self.answer02(nums)

    def answer01(self, nums: List[int]) -> int:
        mem = [False] * len(nums)
        for n in nums:
            if (0 < n) and (n <= len(nums)):
                mem[n-1] = True

        print(mem)
        for i in range(len(nums)):
            if not mem[i]:
                return i+1
        return len(nums)+1

    def answer02(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/first-missing-positive/discuss/1162430
        # 1. Remove the irrelevant numbers from the array
        # 2. Pick the element nums[i] and make the element of nums[i]-1 as negative.
        # 3. if it is irrelevant number skip that 2 step.
        #    irrelevant means ==> values less than 0 and greater than len(nums)
        # 4. Now iterate through the array if you found any positive value return that index+1 
        # 5. if nothing has come just return len(nums)+1 as answer
        x = 2**32
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = x
        for i in range(n):
            val = abs(nums[i])
            if val != x and nums[val-1] > 0:
                nums[val-1] = -nums[val-1]
        print(nums)
        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        nums = [1, 2, 0]
        expected = 3
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test02(self):
        nums = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test03(self):
        nums = [7, 8, 9, 11, 12]
        expected = 1
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test04(self):
        nums = [1]
        expected = 2
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)

    def test05(self):
        nums = [4, 9, 8, 6, 5, 3, 4, 1]
        expected = 2
        self.assertEqual(self.solution.firstMissingPositive(nums), expected)


if __name__ == "__main__":
    unittest.main()
