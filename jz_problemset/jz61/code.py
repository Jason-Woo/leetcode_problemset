# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def Serialize(self, root):
        # write code here
        if root is None:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        root, _ = self.dfs(s.split(','), 0)
        return root

    def dfs(self, s, pos):
        if s[pos] == '#':
            return None, pos + 1
        root = TreeNode(int(s[pos]))
        pos += 1
        root.left, pos = self.dfs(s, pos)
        root.right, pos = self.dfs(s, pos)
        return root, pos