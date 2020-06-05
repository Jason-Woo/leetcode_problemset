class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr_num = nums[0]
        size = 1
        for i in range(len(nums)):
            if nums[i] != curr_num:
                nums[size] = nums[i]
                curr_num = nums[i]
                size += 1
        return size

