class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x0 = x
        result = 0
        if x < 0:
            return False
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        return x0 == result

s = Solution()
s.isPalindrome(1123)