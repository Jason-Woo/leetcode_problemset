import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq = [i for i in range(1, n + 1)]
        return self.iter_permutation(seq, k)

    def iter_permutation(self, seq, k):
        if len(seq) == 1:
            return str(seq[0])
        tmp = math.factorial(len(seq) - 1)
        tmp1 = (k - 1) // tmp
        tmp2 = k - tmp * tmp1
        target = seq[tmp1]
        seq.remove(target)

        tmp3 = self.iter_permutation(seq, tmp2)
        return str(target) + tmp3