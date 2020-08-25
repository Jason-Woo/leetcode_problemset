# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        flag = [0 for _ in range(len(numbers))]
        for i in range(len(numbers)):
            if flag[numbers[i]] != 0:
                duplication[0] = numbers[i]
                return True
            else:
                flag[numbers[i]] += 1
        return False
