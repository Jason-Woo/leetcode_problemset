# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m, n = len(array) - 1, len(array[0]) - 1
        curr_x, curr_y = m, 0
        while curr_x >= 0 and curr_y <= n:
            if array[curr_x][curr_y] == target:
                return True
            elif array[curr_x][curr_y] < target:
                curr_y += 1
            elif array[curr_x][curr_y] > target:
                curr_x -= 1
        return False