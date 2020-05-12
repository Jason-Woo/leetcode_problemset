class Solution(object):
    def judgePalindrome(self, str):
        if str[0] == str[-1]: #atten
            return True
        else:
            return False

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = -1
        result = None
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s):
                # print(i-j,i+j,s[i-j:i+j+1])
                if self.judgePalindrome(s[i-j:i+j+1]):
                    if 2 * j > max_len:
                        result = s[i-j: i+j+1]
                        max_len = 2 * j
                    j += 1
                else:
                    break
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + 1 + j < len(s):
                if self.judgePalindrome(s[i-j:i+j+2]):
                    if 2 * j + 1 > max_len:
                        result = s[i-j:i+j+2]
                        max_len = 2 * j + 1
                    j += 1
                else:
                    break
        return result

s = Solution()
print(s.longestPalindrome('babad'))