# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        self.max_depth = 0
        self.dfs(pRoot, 0)
        return self.max_depth

    def dfs(self, node, depth):
        if node is None:
            self.max_depth = max(self.max_depth, depth)
            return
        else:
            self.dfs(node.left, depth + 1)
            self.dfs(node.right, depth + 1)
