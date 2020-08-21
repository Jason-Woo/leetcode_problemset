# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [-1 for _ in range(len(array))]
        dp[0] = array[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i - 1] + array[i], array[i])
        return max(dp)

s = Solution()
print(s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))