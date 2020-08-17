class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        i, j = 0, len(rotateArray) - 1
        while i < j - 1:
            mid = (i + j) // 2
            if rotateArray[mid] >= rotateArray[i]:
                i = mid
            else:
                j = mid
        return min(rotateArray[i], rotateArray[j])