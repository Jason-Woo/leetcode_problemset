
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        results = False
        if pRoot1 is None or pRoot2 is None:
            return False
        if pRoot1.val == pRoot2.val:
            results = self.isSubTree(pRoot1, pRoot2)
        if results is False:
            results = self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)

        return results

    def isSubTree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        else:
            return self.isSubTree(pRoot1.left, pRoot2.left) & self.isSubTree(pRoot1.right, pRoot2.right)
