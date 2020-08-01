class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals_sorted = sorted(intervals, key=lambda j: j[0])
        ans = [intervals_sorted[0]]
        for i in intervals_sorted:
            if i[0] <= ans[-1][1]:
                ans[-1][1] = max(i[1], ans[-1][1]) #Atten
            else:
                ans.append(i)
        return ans