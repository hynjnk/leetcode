#! /usr/bin/env python3

# twoSum_naive  : brute force
# twoSum_dict   : using solution 3 - One-pass Hash Table https://leetcode.com/problems/two-sum/solution/


class Solution:
    def twoSum(self, nums, target):
        return self.twoSum_dict(nums, target)

    def twoSum_naive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype target; List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_dict(self, nums, target):
        numsDict = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in numsDict:
                return [i, numsDict[complement]]
            else:
                numsDict[v] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
    print(Solution().twoSum_dict(nums, target))
