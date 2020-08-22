# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        num2, num3, num5 = 0, 0, 0
        ans_list = [1]
        while len(ans_list) < index:
            n2 = ans_list[num2] * 2
            n3 = ans_list[num3] * 3
            n5 = ans_list[num5] * 5
            ans_list.append(min(n2, n3, n5))
            if ans_list[-1] == n2:
                num2 += 1
            if ans_list[-1] == n3:
                num3 += 1
            if ans_list[-1] == n5:
                num5 += 1
        return ans_list[-1]
