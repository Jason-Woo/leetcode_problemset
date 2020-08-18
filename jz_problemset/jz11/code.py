# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n >= 0:
            return bin(n).count("1")
        else:
            return bin(~ (n & 0xffffffff) + 1).count("1")

# a = 1
# b = -1
# print(bin(a & 0xffffffff))  0b1
# print(bin(b & 0xffffffff))  0b11111111111111111111111111111111
# print(bin(~(b & 0xffffffff)))   -0b100000000000000000000000000000000
# print(bin(~(b & 0xffffffff) + 1))   -0b11111111111111111111111111111111
