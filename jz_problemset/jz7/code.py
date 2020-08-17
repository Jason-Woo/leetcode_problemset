# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        fib = [0, 1]
        if n <= 1:
            return fib[n]
        cnt = 1
        while cnt < n:
            fib.append(fib[-1] + fib[-2])
            cnt += 1
        return fib[-1]