class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        if numRows == 1: #Atten
            return s
        num_group = len(s) // (2 * numRows - 2)
        for j in range(numRows):
            for i in range(num_group + 1):
                pos1 = i * (2 * numRows - 2) + j
                if j == 0 or j == numRows - 1:
                    if pos1 < len(s):
                        result += s[pos1]
                else:
                    pos2 = (i + 1) * (2 * numRows - 2) - j
                    if pos1 < len(s):
                        result += s[pos1]
                    if pos2 < len(s):
                        result += s[pos2]
        return result

s = Solution()
print(s.convert("PAYPALISHIRING",3))