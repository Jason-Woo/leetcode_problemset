class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_len = len(s)
        opt_l, opt_r = 0, 0
        d = {}

        left, right = 0, 0
        for tt in t:
            d[tt] = d.get(tt, 0) + 1
