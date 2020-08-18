# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None
        tmp_node = pHead
        prev_node = None
        next_node = None
        while tmp_node.next is not None:
            next_node = tmp_node.next
            tmp_node.next = prev_node
            prev_node = tmp_node
            tmp_node = next_node
        tmp_node.next = prev_node
        return tmp_node