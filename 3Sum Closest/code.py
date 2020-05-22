class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k and j < len(nums) and k > i:
                print(nums[i], nums[j], nums[k])
                if abs((nums[i] + nums[j] + nums[k]) - target) < abs(result - target):
                    result = nums[i] + nums[j] + nums[k]
                if nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
        return result

s = Solution()
print(s.threeSumClosest([0,2,1,-3],1))