class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        inf = 999999999
        len_1 = len(nums1)
        len_2 = len(nums2)
        nums1.extend([inf, inf, inf, inf, inf, inf, inf])
        nums2.extend([inf, inf, inf, inf, inf, inf, inf])
        if (len_1 + len_2) % 2 != 0:
            pos = (len_1 + len_2) // 2 + 1
            p1, p2 = -1, -1
            cnt = 0
            while cnt < pos - 1:
                if nums1[p1 + 1] < nums2[p2 + 1]:
                    p1 += 1
                    cnt += 1
                else:
                    p2 += 1
                    cnt += 1
            return min(nums1[p1 + 1], nums2[p2 + 1])

        else:
            pos = (len_1 + len_2) // 2
            p1, p2 = -1, -1
            cnt = 0
            while cnt < pos - 1:
                if nums1[p1 + 1] < nums2[p2 + 1]:
                    p1 += 1
                    cnt += 1
                else:
                    p2 += 1
                    cnt += 1
            if nums1[p1 + 1] < nums2[p2 + 1]:
                result = nums1[p1 + 1]
                p1 += 1
            else:
                result = nums2[p2 + 1]
                p2 += 1
            return float(result + min(nums1[p1 + 1], nums2[p2 + 1])) / 2