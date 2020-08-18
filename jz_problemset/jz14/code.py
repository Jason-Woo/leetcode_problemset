# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return head
        if k == 0:
            return None
        p0 = head
        p1 = head
        for _ in range(k - 1):
            p0 = p0.next
            if p0 is None:
                return None
        while p0.next is not None:
            p0 = p0.next
            p1 = p1.next
        return p1