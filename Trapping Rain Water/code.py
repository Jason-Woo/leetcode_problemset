class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_max, r_max, h, ans = 0, 0, [], 0
        for ele in height:
            if ele > l_max:
                l_max = ele
            h.append(l_max)
        for i in range(len(height) - 1, -1, -1):
            if height[i] > r_max:
                r_max = height[i]
            ans += min(r_max, h[i]) - height[i]
        return ans
