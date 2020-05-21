# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC')
        s = s.replace('XC', 'LXXXX').replace('XL', 'XXXX')
        s = s.replace('IX', 'VIIII').replace('IV', 'IIII')
        result = 0
        for i in range(len(s)):
            if s[i] == 'M': result += 1000
            elif s[i] == 'D': result += 500
            elif s[i] == 'C': result += 100
            elif s[i] == 'L': result += 50
            elif s[i] == 'X': result += 10
            elif s[i] == 'V': result += 5
            elif s[i] == 'I': result += 1
        return result
