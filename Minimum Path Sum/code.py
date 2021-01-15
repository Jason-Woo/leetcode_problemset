class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                min_cost = 9999999
                if i > 0:
                    min_cost = min(min_cost, dp[i - 1][j] + grid[i - 1][j])
                if j > 0:
                    min_cost = min(min_cost, dp[i][j - 1] + grid[i][j - 1])
                dp[i][j] = min_cost
        return dp[-1][-1] + grid[-1][-1]