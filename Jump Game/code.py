# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         self.nums = nums
#         self.n = len(nums)
#         if self.dfs(0):
#             return True
#         else:
#             return False
#
#     def dfs(self, pos):
#         if pos >= self.n - 1:
#             return True
#         for i in range(1, self.nums[pos] + 1):
#             if self.dfs(pos + i):
#                 return True

# Time limit exceed

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end = 0
        for i in range(len(nums)):
            if i > end:
                return False
            end = max(end, i + nums[i])
        return True

