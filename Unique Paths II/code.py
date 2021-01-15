class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path_cnt = [[0 for _ in range(n)] for _ in range(m)]
        path_cnt[0][0] = 1
        if obstacleGrid[0][0] == 0:
            path_cnt[0][0] = 1
        else:
            return 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0:
                    path_cnt[i][j] += path_cnt[i - 1][j]
                if j > 0:
                    path_cnt[i][j] += path_cnt[i][j - 1]
        return path_cnt[-1][-1]