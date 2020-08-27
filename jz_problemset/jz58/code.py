# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
             return True
        return self.Symmetrical(pRoot.left, pRoot.right)
    def Symmetrical(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return left.val == right.val and self.Symmetrical(left.left, right.right) and self.Symmetrical(left.right, right.left)

