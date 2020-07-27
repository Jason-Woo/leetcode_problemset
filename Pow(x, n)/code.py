class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.d = {} #Atten set d global
        if n == 0:
            return 1
        elif n < 0:
            return self.mPow(1 / x, -1 * n)
        else:
            return self.mPow(x, n)

    def mPow(self, x, n):
        if n == 1:
            return x
        elif n > 1:
            n1 = n // 2
            n2 = n - n1
            num1, num2 = self.d.get(n1), self.d.get(n2)
            if num1 is None:
                num1 = self.mPow(x, n1)
                self.d[n1] = num1
            if num2 is None:
                num2 = self.mPow(x, n2)
                self.d[n2] = num2
            return num1 * num2
