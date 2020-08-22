# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = {}
        for num in array:
            if num in d.keys():
                del d[num]
            else:
                d[num] = 1
        return list(d.keys())