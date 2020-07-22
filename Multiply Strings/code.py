class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = self.stoi(num1) * self.stoi(num2)
        return self.itos(ans)


    def stoi(self, num):
        ans = 0
        for i in range(len(num)):
            s = ord(num[i]) - 48
            ans += s * pow(10, len(num) - i - 1)
        return ans

    def itos(self, num):
        ans = ''
        if num == 0:
            return '0'
        while num != 0:
            i = num % 10
            ans = chr(i + 48) + ans
            num = num // 10
        return ans