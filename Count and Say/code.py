class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            result = ''
            prev_str = self.countAndSay(n - 1)
            num = prev_str[0]
            cnt = 1
            for i in range(1, len(prev_str) + 1):
                if i < len(prev_str):
                    if prev_str[i] == num:
                        cnt += 1
                    else:
                        result += str(cnt) + num
                        num = prev_str[i]
                        cnt = 1
                else:
                    result += str(cnt) + num
            return result
