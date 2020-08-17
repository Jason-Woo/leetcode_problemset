# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        dp = [-1 for _ in range(number + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]