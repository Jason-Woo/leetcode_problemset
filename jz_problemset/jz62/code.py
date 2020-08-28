# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        l = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            l.append(node)
            dfs(node.right)

        dfs(pRoot)
        if len(l) < k or k <= 0:
            return None
        else:
            return l[k - 1]