# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []
        self.ans = []
        ss_sorted = sorted(ss)
        self.iter_permutation(ss, '')
        return self.ans

    def iter_permutation(self, ss, path):
        if len(ss) == 0:
            self.ans.append(path)
            return
        for i in range(len(ss)):
            if i == 0:
                self.iter_permutation(ss[1:], path + ss[0])
            elif ss[i] != ss[i - 1]:
                self.iter_permutation(ss[:i] + ss[i + 1:], path + ss[i])
