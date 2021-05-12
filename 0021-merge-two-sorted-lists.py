# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = cur.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = cur.next

        if not l1:
            cur.next = l2
            return dummy.next
        else:  # l2 is None
            cur.next = l1
            return dummy.next
