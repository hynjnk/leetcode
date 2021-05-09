from typing import List

'''
class Solution50ms:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        L = len(nums)
        N = {j: i for i, j in enumerate(nums)}
        S = set()
        M = nums[-1]
        for i in range(L-3):
            a = nums[i]
            if a + 3*M < target:
                continue
            if 4*a > target:
                break
            for j in range(i+1, L-2):
                b = nums[j]
                if a + b + 2*M < target:
                    continue
                if a + 3*b > target:
                    break
                for k in range(j+1, L-1):
                    c = nums[k]
                    d = target-(a+b+c)
                    if d > M:
                        continue
                    if d < c:
                        break
                    if d in N and N[d] > k:
                        S.add((a, b, c, d))
        return S
'''


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        two_sums_dict = dict()
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s in two_sums_dict:
                    two_sums_dict[s].append([i, j])
                else:
                    two_sums_dict[s] = [[i, j]]

        result_set = set()
        two_sums = sorted(two_sums_dict)
        left = 0
        right = len(two_sums) - 1
        while left <= right:
            s = two_sums[left] + two_sums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                left_sum = two_sums[left]
                right_sum = two_sums[right]
                litems = sorted(
                    two_sums_dict[left_sum], key=lambda l: l[1])
                ritems = sorted(
                    two_sums_dict[right_sum], key=lambda r: r[0], reverse=True)
                for lnumbers in litems:
                    for rnumbers in ritems:
                        i0 = lnumbers[0]
                        i1 = lnumbers[1]
                        i2 = rnumbers[0]
                        i3 = rnumbers[1]
                        if i1 >= i2:
                            break
                        result_set.add(
                            (nums[i0], nums[i1], nums[i2], nums[i3]))
                left += 1
                right -= 1

        return list(map(
            lambda t: list(t),
            list(result_set)
        ))


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum(
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        8
    ))
    print(solution.fourSum(
        [1, 0, -1, 0, -2, 2],
        0
    ))
