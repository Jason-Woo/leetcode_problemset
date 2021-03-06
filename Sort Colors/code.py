class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        color0, color1, color2 = 0, 0, 0
        for ele in nums:
            if ele == 0:
                color0 += 1
            elif ele == 1:
                color1 += 1
            else:
                color2 += 1
        for i in range(len(nums)):
            if color0 > 0:
                nums[i] = 0
                color0 -= 1
            elif color1 > 0:
                nums[i] = 1
                color1 -= 1
            elif color2 > 0:
                nums[i] = 2
                color2 -= 1
