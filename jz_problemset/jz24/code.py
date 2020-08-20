# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.ans = []
        if root is None:
            return self.ans
        self.bfs_findpath(root, expectNumber, [])
        return self.ans

    def bfs_findpath(self, node, value, path):
        if node.val == value and not node.left and not node.right:
            self.ans.append(path + [node.val])
            return
        if node.left is not None:
            self.bfs_findpath(node.left, value - node.val, path + [node.val])
        if node.right is not None:
            self.bfs_findpath(node.right, value - node.val, path + [node.val])