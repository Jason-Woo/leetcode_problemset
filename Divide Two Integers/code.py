class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_num = pow(2, 31) - 1
        min_num = -1 * pow(2, 31)
        result = int(float(dividend) / float(divisor))
        print(min_num, max_num)
        if min_num <= result <= max_num:
            return result
        else:
            return max_num