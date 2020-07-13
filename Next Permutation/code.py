class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        i = len(nums) - 1
        j = i
        while i > 0 and nums[i - 1] > nums[i]:
            i -= 1
        if i == 0:
            return nums.reverse()
        i -= 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[:i:-1]
        return nums
