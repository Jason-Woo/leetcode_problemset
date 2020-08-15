# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        tar = '%20'
        l = len(s) - 1
        i = 0
        while i <= l:
            if s[i] == ' ':
                s = s[:i] + tar + s[i + 1:]
                i += 2
                l = len(s) - 1
            i += 1
        return s
