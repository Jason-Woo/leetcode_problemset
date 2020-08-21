# -*- coding:utf-8 -*-
import heapq

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)
