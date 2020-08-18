# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(-1)
        last_node = head
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                new_node = ListNode(pHead1.val)
                last_node.next = new_node
                last_node = new_node
                pHead1 = pHead1.next
            else:
                new_node = ListNode(pHead2.val)
                last_node.next = new_node
                last_node = new_node
                pHead2 = pHead2.next
        if pHead2 is not None:
            last_node.next = pHead2
        elif pHead1 is not None:
            last_node.next = pHead1
        else:
            return None
        return head.next
