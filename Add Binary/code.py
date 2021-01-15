class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        over_flow = 0
        ans = ''
        while i >= 0 or j >= 0:
            new_num = over_flow
            if i >= 0:
                new_num += int(a[i])
            if j >= 0:
                new_num += int(b[j])
            if new_num >= 2:
                new_num -= 2
                over_flow = 1
            else:
                over_flow = 0
            ans = str(new_num) + ans
            i -= 1
            j -= 1
        if over_flow == 1:
            ans = '1' + ans
        return ans
