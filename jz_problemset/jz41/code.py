# -*- coding:utf-8 -*-
import math

class Solution:
    # n**2 + (2A+1)n +2A-2tsum = 0

    def solve(self, a, tsum):
        delta = math.sqrt(4 * a * a - 4 * a + 8 * tsum + 1)
        if delta.is_integer():
            n = (-2 * a - 1 + delta) / 2
            if n.is_integer():
                return n
        return -1

    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []

        for i in range(1, tsum):
            n = int(self.solve(i, tsum))
            if n != -1:
                tmp_ans = [i + j for j in range(n + 1)]
                ans.append(tmp_ans)
        return ans