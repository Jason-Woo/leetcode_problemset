# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [],[]
        tmp_node1, tmp_node2 = pHead1, pHead2
        while tmp_node1:
            stack1.append(tmp_node1)
            tmp_node1 = tmp_node1.next

        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        ans = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 == top2:
                ans = top1
            else:
                break
        return ans