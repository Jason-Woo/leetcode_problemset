# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        b = [-1 for _ in range(len(A))]
        b[0] = 1
        for i in range(1, len(A)):
            b[i] = b[i - 1] * A[i - 1]
        tmp = 1
        for i in range(len(A) - 1, -1, -1):
            b[i] *= tmp
            tmp *= A[i]
        return b