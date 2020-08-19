# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            if not pushV and popV[0] != stack[-1]:
                return False
            if not stack or popV[0] != stack[-1]:
                stack.append(pushV.pop(0))
            else:
                popV.pop(0)
                stack.pop()
        return True

a = [1,2,3,4,5]
b = [4,5,3,2,1]
c = [4,3,5,1,2]
d = [1,2,3,4,5]
s = Solution()
print(s.IsPopOrder(a, c))
