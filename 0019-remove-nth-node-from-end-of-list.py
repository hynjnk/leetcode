import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        now = head
        i = 1
        before = now
        after = now
        while now is not None:
            now = now.next
            if i > n - 1:
                after = after.next
            if i > n + 1:
                before = before.next
            i += 1

        if n < i - 1:  # if n is smaller than length of the ListNode
            before.next = after
            return head
        else:  # if n is same or bigger than length of the ListNode
            return after


def listToListNode(elements: List) -> ListNode:
    head = None
    for element in reversed(elements):
        head = ListNode(element, head)
    return head


def listNodeToList(head: ListNode) -> List:
    elements = []
    while head is not None:
        # print('head.val', head.val)
        elements.append(head.val)
        head = head.next
    return elements


class TestSolution(unittest.TestCase):
    solution = Solution()

    def testListToListNone(self):
        elements = [1, 2, 3, 4, 5]
        head = listToListNode(elements)
        recovered = listNodeToList(head)
        self.assertEqual(elements, recovered)

    def test01(self):
        head = listToListNode(
            [1, 2, 3, 4, 5]
        )
        n = 2
        expected = [1, 2, 3, 5]
        self.assertEqual(
            listNodeToList(self.solution.removeNthFromEnd(head, n)),
            expected
        )

    def test02(self):
        head = listToListNode(
            [1]
        )
        n = 1
        expected = []
        self.assertEqual(
            listNodeToList(self.solution.removeNthFromEnd(head, n)),
            expected
        )

    def test03(self):
        head = listToListNode(
            [1, 2]
        )
        n = 1
        expected = [1]
        self.assertEqual(
            listNodeToList(self.solution.removeNthFromEnd(head, n)),
            expected
        )

    def test04(self):
        head = listToListNode(
            [1, 2]
        )
        n = 2
        expected = [2]
        self.assertEqual(
            listNodeToList(self.solution.removeNthFromEnd(head, n)),
            expected
        )


if __name__ == '__main__':
    unittest.main()
