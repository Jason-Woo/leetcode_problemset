class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        candidate = [i for i in range(1, n+1)]
        ans = []
        tmp_ans = []
        iter_combine(k, candidate, ans, tmp_ans)
        return ans


def iter_combine(depth, candidate, ans, tmp_ans):
    if depth == 0:
        ans.append(tmp_ans)
    if len(candidate) == 1:
        tmp_ans.append(candidate[0])
        ans.append(tmp_ans)
    else:
        for i, can in enumerate(candidate):
            tmp_ans.append(can)
            iter_combine(depth-1, candidate[:i]+candidate[i+1:], ans, tmp_ans)