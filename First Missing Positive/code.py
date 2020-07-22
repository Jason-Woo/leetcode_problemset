import numpy as np

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            if nums[i] == ans:
                    ans += 1
            else:
                return ans
        return ans


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = [1]
        for i in range(len(nums) + 2):
            dic.append(0)
        for num in nums:
            if 0 <= num < len(dic):
                dic[num] = 1
        for i in range(len(dic)):
            if dic[i] == 0:
                return i