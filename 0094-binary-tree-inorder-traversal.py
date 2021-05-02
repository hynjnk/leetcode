from __future__ import annotations  # Python 3.7+ < 3.10
import unittest
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def fromList(int_list: List[int]) -> TreeNode:
        ''' Breadth First or Level Order Traversal list to TreeNode '''
        q = deque()
        for val in int_list:
            if val is not None:
                q.append(TreeNode(val))
            else:
                q.append(val)

        if not q:
            return None

        root_level = [q.popleft()]
        TreeNode.add_leaves(root_level, q)
        return root_level[0]

    def add_leaves(nodes: List[TreeNode], q: deque[TreeNode]):
        next_level = []
        for node in nodes:
            if not q:
                return
            node.left = q.popleft()
            if node.left:
                next_level.append(node.left)

            if not q:
                return
            node.right = q.popleft()
            if node.right:
                next_level.append(node.right)

        if next_level:
            TreeNode.add_leaves(next_level, q)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        root = TreeNode.fromList([1, None, 2, 3])
        expected = [1, 3, 2]
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)

    def test02(self):
        root = TreeNode.fromList([])
        expected = []
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)

    def test03(self):
        root = TreeNode.fromList([1])
        expected = [1]
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)

    def test04(self):
        root = TreeNode.fromList([1, 2])
        expected = [2, 1]
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)

    def test05(self):
        root = TreeNode.fromList([1, None, 2])
        expected = [1, 2]
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)

    def test06(self):
        root = TreeNode.fromList([1, 2, 3, 4, 5, 6, 7])
        expected = [4, 2, 5, 1, 6, 3, 7]
        inorderTraversal = self.solution.inorderTraversal(root)
        self.assertEqual(inorderTraversal, expected)


if __name__ == "__main__":
    unittest.main()
