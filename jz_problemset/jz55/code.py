# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return None
        node_fast = pHead.next.next
        node_slow = pHead.next
        while node_fast != node_slow:
            if node_fast is None or node_fast.next is None:
                return None
            node_fast = node_fast.next.next
            node_slow = node_slow.next
        node_fast = pHead
        while node_fast != node_slow:
            node_fast = node_fast.next
            node_slow = node_slow.next
        return node_slow

