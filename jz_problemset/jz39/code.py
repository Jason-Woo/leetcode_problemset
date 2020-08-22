# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.is_balanced = True
        self.dfs(pRoot, 0)
        return self.is_balanced

    def dfs(self, node, depth):
            if node is None:
                return depth
            else:
                depth_l = self.dfs(node.left, depth + 1)
                depth_r = self.dfs(node.right, depth + 1)
                if abs(depth_l - depth_r) > 1:
                    self.is_balanced = False
                return max(depth_l, depth_r)