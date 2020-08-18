
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False

        # 根节点以pRoot2为主，判断pRoot2是否和当前pRoot1节点后的相同
        def hasEqual(pRoot1, pRoot2):
            if not pRoot1:
                return False
            if not pRoot2:
                return False
            if pRoot1.val == pRoot2.val:  # 根节点相同的话再去分别判断左右子树是否相同
                if pRoot2.left == None:
                    leftEqual = True
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left)
                if pRoot2.right == None:
                    rightEqual = True
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right)
                return leftEqual and rightEqual
            return False

        ret = hasEqual(pRoot1, pRoot2)
        if ret:
            return True

        # 判断pRoot1的左子树包不包含pRoot2
        ret = self.HasSubtree(pRoot1.left, pRoot2)
        if ret:
            return True
        # 判断pRoot1的右子树包不包含pRoot2
        ret = self.HasSubtree(pRoot1.right, pRoot2)
        if ret:
            return True

Tree1 = TreeNode(1)
l11 = TreeNode(2)
l12 = TreeNode(3)
Tree1.left = l11
Tree1.right = l12

Tree2 = TreeNode(1)
l20 = TreeNode(1)
l21 = TreeNode(2)
l22 = TreeNode(3)
Tree2.right = l20
l20.left = l21
l20.right = l22

s = Solution()
print(s.HasSubtree(Tree1, l20))