class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        common = True
        j = 0
        if not strs:  # Atten
            return result
        if len(strs) == 1:  # Atten
            return strs[0]
        while common:
            for i in range(len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    common = False
                    break
            if common and j < len(strs[0]):
                result += strs[0][j]
            j += 1
        return result
