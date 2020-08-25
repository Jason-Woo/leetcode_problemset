# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return -1
        l = [i for i in range(n)]
        p = m - 1
        while len(l) > 1:
            p %= len(l)
            del l[p]
            p += (m - 1)
        return l[0]