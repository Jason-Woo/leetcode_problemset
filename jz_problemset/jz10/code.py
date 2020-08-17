# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        dp = [-1 for _ in range(number + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]