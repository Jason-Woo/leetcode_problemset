# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ans = []
        if not matrix:
            return ans
        # write code here
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and up <= down:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            if up <= down:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[down][i])
                down -= 1
            if left <= right:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans