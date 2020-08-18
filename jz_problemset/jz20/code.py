# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_val = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_val:
            self.min_val.append(min(self.min_val[-1], node))
        else:
            self.min_val.append(node)
    def pop(self):
        # write code here
        self.min_val.pop()
        return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.min_val[-1]