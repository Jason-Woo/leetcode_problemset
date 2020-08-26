# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(pattern) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        if len(s) == 0:
            if len(pattern) == 2 and pattern[-1] == '*':
                return True
            else:
                return False
        if pattern[-1] == '.':
            return self.match(s[:-1], pattern[:-1])
        elif pattern[-1] == '*':
            if pattern[-2] == '.':
                return True
            is_match = self.match(s, pattern[:-2])
            i = -1
            while i >= -1 * len(s) and s[i] == pattern[-2]:
                is_match |= self.match(s[:i], pattern[:-2])
                i -= 1
            return is_match
        else:
            if pattern[-1] == s[-1]:
                return self.match(s[:-1], pattern[:-1])
            else:
                return False