# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        hash_list = [0 for _ in range(58)]
        for i in range(len(s)):
            hash_list[ord(s[i]) - 65] += 1
        for i in range(len(s)):
            if hash_list[ord(s[i]) - 65] == 1:
                return i
        return -1