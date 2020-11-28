#! /usr/bin/env python3
# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = 0
        rDummy = ListNode(-1)
        r = rDummy
        while (l1 is not None) or (l2 is not None) or temp:
            if l1 is None:
                l1v = 0
            else:
                l1v = l1.val
            if l2 is None:
                l2v = 0
            else:
                l2v = l2.val
            temp = l1v + l2v + temp
            temp, remain = divmod(temp, 10)
            r.next = ListNode(remain)
            r = r.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return rDummy.next

'''
if __name__ == '__main__':
    a = ListNode([3, 4, 5])
    print(a.val)
    print(a.next)
'''
