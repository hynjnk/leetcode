# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if head is None:
            return

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        asc_cur = head
        while True:
            asc_next = asc_cur.next
            desc_cur = stack.pop()

            if asc_cur == desc_cur:
                asc_cur.next = None
                return
            asc_cur.next = desc_cur

            if desc_cur == asc_next:
                desc_cur.next = None
                return
            desc_cur.next = asc_next
            asc_cur = asc_next
