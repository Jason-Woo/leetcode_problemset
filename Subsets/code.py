class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        subsets_helper(nums, ans, [])
        return ans


def subsets_helper(nums, ans, tmp_ans):
    ans.append(tmp_ans)
    for i, num in enumerate(nums):
        subsets_helper(nums[i+1:], ans, tmp_ans+[num])