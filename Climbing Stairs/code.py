class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n)]
        dp[0] = 1
        if n > 1:
            dp[1] = 1
        for i in range(n):
            if i - 1 >= 0:
                dp[i] += dp[i - 1]
            if i - 2 >=0:
                dp[i] += dp[i - 2]
        return dp[-1]