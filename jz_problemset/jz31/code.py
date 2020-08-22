# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cur = n % 10
        high, low = n//10, 0
        digit, count = 1, 0
        while high != 0 or cur != 0:
            if cur == 0:
                count = high * digit + count
            if cur == 1:
                count += high * digit + low + 1
            if cur > 1:
                count += (high + 1) * digit
            low = low + cur * digit
            cur = high % 10
            high = high // 10
            digit = digit * 10
        return count
