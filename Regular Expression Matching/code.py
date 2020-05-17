class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        tbl = [[False for _ in range(len(p)+1)]for _ in range(len(s)+1)]
        tbl[0][0] = True
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                tbl[0][i] = tbl[0][i - 2]
            else:
                tbl[0][i] = False
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    tbl[i][j] = tbl[i - 1][j - 1]
                if p[j - 1] == '*':
                    tbl[i][j] = tbl[i][j] or tbl[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        tbl[i][j] = tbl[i][j] or tbl[i - 1][j]
        return tbl[len(s)][len(p)]


