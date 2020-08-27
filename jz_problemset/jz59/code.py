# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.queue = []
        self.ans = []

    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        self.queue.append(pRoot)
        self.bfs(1)
        return self.ans

    def bfs(self, depth):
        num = []
        new_queue = []

        while self.queue:
            tmp_node = self.queue.pop(0)
            num.append(tmp_node.val)
            if tmp_node.left:
                new_queue.append(tmp_node.left)
            if tmp_node.right:
                new_queue.append(tmp_node.right)
        if num:
            if depth % 2 == 1:
                self.ans.append(num)
            else:
                num.reverse()
                self.ans.append(num)
        if new_queue:
            self.queue.extend(new_queue)
            self.bfs(depth + 1)
