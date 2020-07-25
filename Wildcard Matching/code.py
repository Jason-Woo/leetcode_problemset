# class Solution(object): Time limit exceed
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(p) <= 1:
#             if p == '':
#                 return p == s
#             if p == '?':
#                 if len(s) == 1:
#                     return True
#             elif p == '*':
#                 return True
#             else:
#                 if p == s:
#                     return True
#         else:
#             if p[0] == '?':
#                 if len(s) >= 1:
#                     return self.isMatch(s[1:], p[1:])
#                 else:
#                     return False
#             elif p[0] == '*':
#                 if len(s) == 0:
#                     return self.isMatch(s, p[1:])
#                 for i in range(len(s)):
#                     if self.isMatch(s[i:], p[1:]):
#                         return True
#                 return False
#             else:
#                 if len(s) == 0:
#                     return False
#                 if p[0] == s[0]:
#                     return self.isMatch(s[1:], p[1:])


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p == []:
            return True
        dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0] = [0 for _ in range(len(s) + 1)]
        dp[0][0] = 1
        for i in range(1, len(p) + 1):
            if dp[i - 1][0] == 1 and p[i - 1] == '*':
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                for j in range(len(s) + 1):
                    if dp[i - 1][j] == 1:
                        for k in range(j, len(s) + 1):
                            dp[i][k] = 1
                        break
            elif p[i - 1] == '?':
                for j in range(1, len(s) + 1):
                    if dp[i - 1][j - 1] == 1:
                        dp[i][j] = 1
            else:
                for j in range(1, len(s) + 1):
                    if dp[i - 1][j - 1] == 1 and p[i - 1] == s[j - 1]:
                        dp[i][j] = 1
        return bool(dp[len(p)][len(s)])


