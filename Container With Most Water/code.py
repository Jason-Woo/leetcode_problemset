class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_size = 0
        while i < j:
            if height[i] < height[j]:
                max_size = max(max_size, (j - i) * height[i])
                i += 1
            else:
                max_size = max(max_size, (j - i) * height[j])
                j -= 1
        return max_size