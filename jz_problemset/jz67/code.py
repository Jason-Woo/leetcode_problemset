# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number <= 3:
            return number - 1
        dp = [-1 for _ in range(number + 1)]
        for i in range(5):
            dp[i] = i
        for i in range(5, number + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j])
        return dp[number]
