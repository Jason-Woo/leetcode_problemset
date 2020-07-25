# class Solution(object): #Time limit exceed
#     def jump(self, nums):
#         self.nums = nums
#         self.queue = [0]
#         self.cnt = 0
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) <= 1:
#             return 0
#         while self.queue:
#             if self.bfs():
#                 return self.cnt
#
#     def bfs(self):
#         l = len(self.queue)
#         self.cnt += 1
#         for _ in range(l):
#             loc = self.queue.pop(0)
#             for i in range(1, self.nums[loc] + 1):
#                 if loc + i >= len(self.nums) - 1:
#                     return True
#                 self.queue.append(loc + i)


#only need to store start and end for each serach!
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = step = 0
        while end < len(nums) - 1:
            start, end = end + 1, max([i + nums[i] for i in range(start, end + 1)])
            step += 1
        return step
