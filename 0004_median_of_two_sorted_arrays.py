#! /usr/bin/env python3


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.m = len(nums1)
        self.n = len(nums2)
        self.k = (self.m + self.n) // 2
        self.i_min = max(0, self.k - self.n)
        self.i_max = min(self.m, self.k)
        return self.findMedianIterator(self.i_min, self.i_max)

    def findMedianIterator(self, before, toward):
        if toward == before:
            #print("Value error, ", before, toward)
            raise ValueError
        elif toward > before:
            i = (toward + before + 1) // 2
            j = self.k - i
        else:
            i = (toward + before) // 2
            j = self.k - i

        if i == self.i_max or i == self.i_min:
            return self.findMedian(i, j)
        if self.nums1[i - 1] > self.nums2[j]:
            return self.findMedianIterator(i, min(before, toward))
        if self.nums1[i] < self.nums2[j - 1]:
            return self.findMedianIterator(i, max(before, toward))
        return self.findMedian(i, j)

    def findMedian(self, i, j):
        right_min = min(self.nums1[i:i + 1] + self.nums2[j:j + 1])
        if (self.m + self.n) % 2:
            return right_min
        left_max = max(self.nums1[i - 1:i] + self.nums2[j - 1:j])
        return (right_min + left_max) / 2.0

if __name__ == '__main__':
    nums1 = [1, 2, 4, 5, 8, 9]
    nums2 = [0, 3, 6, 7, 10]
    print(Solution().findMedianSortedArrays(nums1, nums2))
