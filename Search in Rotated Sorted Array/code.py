class Solution(object):
    def iter_serach(self, nums, target, i, j):
        if nums[i] == target:
            return i
        if nums[j] == target:
            return j
        if j - i <= 2 and (nums[i] != target or nums[j] != target):
            return None
        ans1 = None
        ans2 = None
        if nums[i] < nums[j]:
            if nums[i] < target < nums[j]:
                mid = (i + j) // 2
                ans1 = self.iter_serach(nums, target, i, mid)
                ans2 = self.iter_serach(nums, target, mid + 1, j)
        else:
            if target > nums[i] or target < nums[j]:
                mid = (i + j) // 2
                ans1 = self.iter_serach(nums, target, i, mid)
                ans2 = self.iter_serach(nums, target, mid + 1, j)
        if ans1 is not None:
            return ans1
        if ans2 is not None:
            return ans2

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        ans = None
        ans = self.iter_serach(nums, target, 0, len(nums) - 1)
        if ans is not None:
            return ans
        else:
            return -1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1
#
#         while l <= r:
#             mid = (l + r) // 2
#             if target == nums[mid]:
#                 return mid
#             # nums[left to mid] is sorted
#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             # nums[mid to right] is sorted
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1
