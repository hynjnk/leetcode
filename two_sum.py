#! /usr/bin/env python3


class Solution:
    def twoSum(self, nums, target):
        return self.twoSum_naive(nums, target)

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
        numsDict = {v: i for i, v in enumerate(nums)}
        for v in nums:
            complement = target - v
            if (complement != v) and (complement in numsDict):
                return [numsDict[v], numsDict[complement]]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
    print(Solution().twoSum_dict(nums, target))
