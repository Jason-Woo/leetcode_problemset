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
        self.queue.append(pRoot)
        self.bfs(1)
        return self.ans

    def bfs(self, depth):
        val = []
        new_queue = []
        while self.queue:
            tmp_node = self.queue.pop(0)
            val.append(tmp_node.val)
            if tmp_node.left:
                new_queue.append(tmp_node.left)
            if tmp_node.right:
                new_queue.append(tmp_node.right)
        if depth % 2 == 1:
            self.ans.extend(val)
        else:
            val.reverse()
            self.ans.extend(val)
        self.queue.extend(new_queue)
        if self.queue:
            self.bfs(depth + 1)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

s = Solution()
print(s.Print(a))