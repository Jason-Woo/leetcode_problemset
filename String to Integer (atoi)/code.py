class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0
        result = ''
        i = 0
        min_int, max_int = -2 ** 31, 2 ** 31 - 1
        while i < len(str) and str[i] == ' ':
            i += 1
        if i >= len(str):
            return 0
        if str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                result += '-'
            i += 1
        while i < len(str) and ord(str[i]) in range(ord('0'), ord('9') + 1):
            result += str[i]
            i += 1
        if result == '' or result == '-':
            return 0
        elif int(result) > max_int:
            return max_int
        elif int(result) < min_int:
            return min_int
        else:
            return int(result)
