import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ref = strs[0]
        while i < len(ref):
            for s in strs[1:]:
                if i >= len(s) or ref[i] != s[i]:
                    return ref[:i]
            i += 1

        return ref[:i]


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test02(self):
        strs = ["dog", "racecar", "car"]
        expected = ""
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)

    def test03(self):
        strs = ["racecar"]
        expected = "racecar"
        self.assertEqual(self.solution.longestCommonPrefix(strs), expected)


if __name__ == "__main__":
    unittest.main()
