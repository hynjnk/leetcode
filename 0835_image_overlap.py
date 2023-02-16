from typing import List
import unittest


class Solution:
    def largestOverlap(self,
                       img1: List[List[int]],
                       img2: List[List[int]]
                       ) -> int:
        # move only img1
        overlap = 0
        for i in range(-len(img1) + 1, len(img1)):
            for j in range(-len(img1[0]) + 1, len(img1[0])):
                overlap = max(overlap, self.calOverlap(img1, img2, i, j))
        return overlap

    def calOverlap(self,
                   img1: List[List[int]],
                   img2: List[List[int]],
                   img1_move_down: int,
                   img1_move_right: int
                   ) -> int:
        if img1_move_down >= 0:
            iRange = range(0, len(img1) - img1_move_down)
        else:
            iRange = range(-img1_move_down, len(img1))
        if img1_move_right >= 0:
            jRange = range(0, len(img1[0]) - img1_move_right)
        else:
            jRange = range(-img1_move_right, len(img1[0]))

        overlap = 0

        for i in iRange:
            for j in jRange:
                if img1[i][j] & img2[i + img1_move_down][j + img1_move_right]:
                    overlap += 1
        return overlap


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
        img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
        expected = 3
        self.assertEqual(self.solution.largestOverlap(img1, img2), expected)

    def test02(self):
        img1 = [[1]]
        img2 = [[1]]
        expected = 1
        self.assertEqual(self.solution.largestOverlap(img1, img2), expected)

    def test03(self):
        img1 = [[0]]
        img2 = [[0]]
        expected = 0
        self.assertEqual(self.solution.largestOverlap(img1, img2), expected)

    def test04(self):
        img1 = [[1]]
        img2 = [[0]]
        expected = 0
        self.assertEqual(self.solution.largestOverlap(img1, img2), expected)

    def test05(self):
        img1 = [[0, 1], [1, 1]]
        img2 = [[1, 1], [1, 0]]
        expected = 2
        self.assertEqual(self.solution.largestOverlap(img1, img2), expected)


if __name__ == '__main__':
    unittest.main()
