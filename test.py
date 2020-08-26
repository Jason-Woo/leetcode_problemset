# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if len(s) == 0:
            return False
        pos = 0
        dot_cnt = 0
        if s[0] == '+' or s[0] == '-':
            pos += 1
        while pos < len(s) and s[pos] != 'E' and s[pos] != 'e':
            if ord(s[pos]) in range(ord('0'), ord('9') + 1):
                pos += 1
            elif s[pos] == '.' and dot_cnt == 0:
                pos += 1
                dot_cnt += 1
            else:
                return False
        if pos == len(s):
            return True
        pos += 1
        if pos == len(s):
            return False
        if s[pos] == '+' or s[pos] == '-':
            pos += 1
        while pos < len(s):
            if ord(s[pos]) in range(ord('0'), ord('9') + 1):
                pos += 1
            else:
                return False
        return True

s = Solution()
print(s.isNumeric("1.2.3"))