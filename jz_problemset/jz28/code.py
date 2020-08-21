# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers_sorted = sorted(numbers)
        target = numbers_sorted[len(numbers) // 2]
        if numbers.count(target) > len(numbers) // 2:
            return target
        else:
            return 0