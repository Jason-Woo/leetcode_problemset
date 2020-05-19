class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a1, remainder = divmod(num, 1000)
        a2, remainder = divmod(remainder, 500)
        a3, remainder = divmod(remainder, 100)
        a4, remainder = divmod(remainder, 50)
        a5, remainder = divmod(remainder, 10)
        a6, a7 = divmod(remainder, 5)
        result = 'M' * a1 + 'D' * a2 + 'C' * a3 + 'L' * a4 + 'X' * a5 + 'V' * a6 + 'I' * a7
        result = result.replace("DCCCC", "CM").replace("CCCC", "CD")
        result = result.replace("LXXXX", "XC").replace("XXXX", "XL")
        result = result.replace("VIIII", "IX").replace("IIII", "IV")
        return result
