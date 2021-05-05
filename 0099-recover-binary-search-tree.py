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

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, TreeNode):
            return (
                self.val == other.val and
                self.left == other.left and
                self.right == other.right
            )
        return False

    def __repr__(self):
        return f"TreeNone val: {self.val}"
        # f"left: {self.left}, right: {self.right}"

    def levelOrderTraversal(self, queue=None, temp_list=None) -> List[int]:
        if not queue:
            return self.levelOrderTraversal([self], [])

        new_queue = []
        for node in queue:
            if not node:
                temp_list.append(node)
                continue

            temp_list.append(node.val)
            new_queue.append(node.left)
            new_queue.append(node.right)

        if new_queue:
            return self.levelOrderTraversal(new_queue, temp_list)
        while temp_list[-1] is None:
            temp_list.pop()
        return temp_list

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
    def recoverTree(self, root: TreeNode) -> None:
        if root is None:
            return

        _, disorders = self.findDisorderedNodes(root, None, [])

        if len(disorders) <= 0:
            # No problem
            return
        n01 = disorders[0][0]
        n02 = disorders[-1][1]

        tmp = n01.val
        n01.val = n02.val
        n02.val = tmp

    def findDisorderedNodes(self, root: TreeNode, last_visited, disorders):
        '''Visit nodes through inorder traversal,
        Return last visited node, tuples of 2 nodes where nodes are disordered.
        '''

        if not root:
            return (last_visited, disorders)

        # check root.left
        last_visited, disorders = self.findDisorderedNodes(
            root.left, last_visited, disorders
        )
        if len(disorders) >= 2:
            return last_visited, disorders

        # check root.val
        if last_visited and last_visited.val > root.val:
            disorders.append((last_visited, root))
        last_visited = root

        if len(disorders) >= 2:
            return last_visited, disorders

        return self.findDisorderedNodes(root.right, last_visited, disorders)


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test01(self):
        root = TreeNode.fromList([1, 3, None, None, 2])
        self.solution.recoverTree(root)

        expected = TreeNode.fromList([3, 1, None, None, 2])
        self.assertEqual(root, expected)

    def test02(self):
        root = TreeNode.fromList([3, 1, 4, None, None, 2])
        self.solution.recoverTree(root)

        expected = TreeNode.fromList([2, 1, 4, None, None, 3])
        self.assertEqual(root, expected)

    def test03(self):
        root = TreeNode.fromList([1, 5])
        self.solution.recoverTree(root)

        expected = TreeNode.fromList([5, 1])
        self.assertEqual(root, expected)

    def test04(self):
        root = TreeNode.fromList([5, None, 1])
        self.solution.recoverTree(root)

        expected = TreeNode.fromList([1, None, 5])
        self.assertEqual(root, expected)

    def test05(self):
        root = TreeNode.fromList([])
        self.solution.recoverTree(root)

        expected = TreeNode.fromList([])
        self.assertEqual(root, expected)


if __name__ == "__main__":
    unittest.main()
