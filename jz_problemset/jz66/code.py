# -*- coding:utf-8 -*-
class Solution:

    def sum_up(self, x):
        ans = 0
        while x != 0:
            ans += x % 10
            x = x // 10
        return ans

    def movingCount(self, threshold, rows, cols):
        # write code here

        mark = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(x, y):
            if self.sum_up(x) + self.sum_up(y) > threshold or x >= rows or y >= cols or mark[x][y]:
                return 0
            else:
                mark[x][y] = 1
                return 1 + dfs(x + 1, y) + dfs(x, y + 1)
        return dfs(0, 0)
