class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        find_word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ' and find_word:
                return cnt
            elif s[i] != ' ':
                find_word = True
                cnt += 1
        if not find_word:
            return 0
        else:
            return cnt