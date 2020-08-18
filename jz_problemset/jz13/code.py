# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        arr_ord = []
        arr_even = []
        for num in array:
            if num % 2 == 0:
                arr_even.append(num)
            else:
                arr_ord.append(num)
        arr_ord.extend(arr_even)
        return arr_ord