class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.path_cnt = [[-1 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            self.path_cnt[0][i] = 1
        for i in range(n):
            self.path_cnt[i][0] = 1
        return self.iter_cnt(m - 1, n - 1)

    def iter_cnt(self, m, n):
        if self.path_cnt[n][m] != -1:
            return self.path_cnt[n][m]
        else:
            if self.path_cnt[n - 1][m] == -1:
                self.path_cnt[n - 1][m] = self.iter_cnt(m, n - 1)
            if self.path_cnt[n][m - 1] == -1:
                self.path_cnt[n][m - 1] = self.iter_cnt(m - 1, n)
            self.path_cnt[n][m] = self.path_cnt[n - 1][m] + self.path_cnt[n][m - 1]
            return self.path_cnt[n][m]