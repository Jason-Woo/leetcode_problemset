# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        tmp_node = listNode
        while tmp_node is not None:
            stack.append(tmp_node.val)
            tmp_node = tmp_node.next
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans