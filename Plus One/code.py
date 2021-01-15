class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        over_flow = True
        while over_flow and i >= 0:
            new_num = digits[i] + 1
            if new_num >= 10:
                new_num -= 10
            else:
                over_flow = False
            digits[i] = new_num
            if over_flow and i == 0:
                return [1] + digits
            i -= 1
        return digits


