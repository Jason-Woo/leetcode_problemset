class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)
