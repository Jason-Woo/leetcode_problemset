# -*- coding:utf-8 -*-
import functools

def comp(a, b):
    if a + b < b + a:
        return -1
    elif a + b > b + a:
        return 1
    else:
        return 0

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        num = map(str, numbers)
        numbers_sorted = sorted(num, key=functools.cmp_to_key(comp))
        return ''.join(numbers_sorted)

s = Solution()
print(s.PrintMinNumber([3,32,321]))