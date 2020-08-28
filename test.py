# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        ans = []
        if len(num) == 0 or size < 1 or len(num) < size:
            return ans
        n = len(num)
        queue = []
        for i in range(n):
            while queue and num[queue[-1]] < num[i]:
                queue.pop()
            queue.append(i)
            if queue[0] + size <= i:
                queue.pop(0)
            if i + 1 >= size:
                ans.append(num[queue[0]])
        return ans



s = Solution()
print(s.maxInWindows([2,3,4,2,6,2,5,1], 3))