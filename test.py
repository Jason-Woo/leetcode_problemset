# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        word = s.split(' ')
        word.reverse()
        return ' '.join(word)
s = Solution()
print(s.ReverseSentence(''))