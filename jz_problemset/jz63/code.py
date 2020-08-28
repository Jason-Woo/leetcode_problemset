# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.queue = []
    def Insert(self, num):
        self.queue.append(num)
    def GetMedian(self, res):
        if len(self.queue) == 0:
            return None
        ans = sorted(self.queue)
        if len(ans) % 2 == 1:
            return ans[len(ans) // 2]
        else:
            return (ans[len(ans) // 2 - 1] + ans[len(ans) // 2]) / 2.0
