# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.cnt = 0
        self.merge_sort(data)
        return self.cnt % 1000000007

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        data1 = self.merge_sort(data[:mid])
        data2 = self.merge_sort(data[mid:])
        p1, p2, p3 = len(data1) - 1, len(data2) - 1, len(data1) + len(data2) - 1
        merge_data = [-1 for _ in range(p3 + 1)]
        while p1 >= 0 or p2 >= 0:
            if p1 < 0:
                merge_data[p3] = data2[p2]
                p2 -= 1
            elif p2 < 0:
                merge_data[p3] = data1[p1]
                p1 -= 1
            elif data1[p1] > data2[p2]:
                merge_data[p3] = data1[p1]
                p1 -= 1
                self.cnt += (p2 + 1)
            else:
                merge_data[p3] = data2[p2]
                p2 -= 1
            p3 -= 1
        return merge_data

s = Solution()
print(s.InversePairs([1,2,3,4,5,6,7,0]))