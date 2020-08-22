# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        l_bound, r_bound = 0, len(data)
        l_tmp, r_tmp = 0, len(data)
        while l_bound < r_tmp:
            mid = (l_bound + r_tmp) // 2
            if data[mid] < k:
                l_bound = mid + 1
            else:
                r_tmp = mid
        while l_tmp < r_bound:
            mid = (l_tmp + r_bound) // 2
            if data[mid] <= k:
                l_tmp = mid + 1
            else:
                r_bound = mid
        return r_bound - l_bound
