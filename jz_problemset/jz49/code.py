# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if len(s) == 0:
            return 0
        ans = 0
        digit = 1
        for i in range(len(s) - 1, 0, -1):
            if ord(s[i]) in range(ord('0'), ord('9')):
                ans += digit * (ord(s[i]) - ord('0'))
                digit *= 10
            else:
                return 0
        if s[0] == '+':
            return ans
        elif s[0] == '-':
            return -1 * ans
        elif ord(s[0]) in range(ord('0'), ord('9')):
            ans += digit * (ord(s[0]) - ord('0'))
            return ans
        else:
            return 0