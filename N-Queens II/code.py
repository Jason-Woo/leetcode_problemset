class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0
        nums = [-1] * n
        self.dfs(nums, 0)
        return self.cnt

    def dfs(self, nums, index):
        if index == len(nums):
            self.cnt += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid_check(nums, index):
                self.dfs(nums, index + 1)

    def valid_check(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[i] - nums[n]) == n - i:
                return False
        return True