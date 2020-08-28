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

# 遍历数组的每一个元素，
# 如果容器为空，则直接将当前元素加入到容器中。
# 如果容器不为空，则让当前元素和容器的最后一个元素比较，如果大于，则将容器的最后一个元素删除，然后继续讲当前元素和容器的最后一个元素比较
# 如果当前元素小于容器的最后一个元素，则直接将当前元素加入到容器的末尾
# 如果容器头部的元素已经不属于当前窗口的边界，则应该将头部元素删除