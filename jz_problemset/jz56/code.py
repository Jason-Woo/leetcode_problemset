# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        v_head = ListNode(-1)
        v_head.next = pHead
        curr_node = v_head.next
        tmp_node = v_head
        while curr_node:
            if curr_node.next and curr_node.val == curr_node.next.val:
                while curr_node.next and curr_node.val == curr_node.next.val:
                    curr_node = curr_node.next
                tmp_node.next = curr_node.next
                curr_node = curr_node.next
            else:
                curr_node = curr_node.next
                tmp_node = tmp_node.next
        return v_head.next