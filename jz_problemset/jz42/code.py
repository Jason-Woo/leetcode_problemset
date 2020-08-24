# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        left, right = 0, len(array) - 1
        while left < right:
            if array[left] + array[right] < tsum:
                left += 1
            elif array[left] + array[right] > tsum:
                right -= 1
            else:
                return [array[left], array[right]]
        return []