class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        while x % 10 == 0 and x != 0:
            x /= 10
        x = int(x)
        if str(x)[0] == '-':
            answer = int('-' + str(x)[1:][::-1])
        else:
            answer = int(str(x)[::-1])
        mina = -2147483648
        maxa = 2147483648
        if answer > maxa or answer < mina: #Atten
            return 0
        else:
            return answer