class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums) - 1
        while r - l > 1:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return r