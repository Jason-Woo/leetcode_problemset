class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def w_dis(i, j):
            if word1[j - 1] == word2[i - 1]:
                return 0
            else:
                return 1
        dp = [[-1 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            dp[i][0] = i
        for i in range(len(word1) + 1):
            dp[0][i] = i
        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, w_dis(i, j) + dp[i - 1][j - 1])
        return dp[len(word2)][len(word1)]
