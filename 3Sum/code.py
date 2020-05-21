# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result = []
#         tmp = set()
#         dict = {}
#         for ele in nums:
#             if ele in dict.keys():
#                 dict[ele] += 1
#             else:
#                 dict[ele] = 1
#         for i in range(len(nums)):
#             dict[nums[i]] -= 1
#             for j in range(i+1, len(nums)):
#                 dict[nums[j]] -= 1
#                 target = -1 * (nums[i] + nums[j])
#                 if target in dict.keys() and dict[target] > 0:
#                     l = sorted([nums[i], nums[j], target])
#                     if str(l[0]) + str(l[1]) + str(l[2]) not in tmp:
#                         result.append(l)
#                         tmp.add(str(l[0]) + str(l[1]) + str(l[2]))
#                 dict[nums[j]] += 1
#             dict[nums[i]] += 1
#         return result

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i] ,nums[l] ,nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0 :
                    l += 1
                else:
                    r -= 1
        return res

s = Solution()
print(s.threeSum([3,0,-2,-1,1,2]))