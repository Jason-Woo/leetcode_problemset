class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] != 1:
            return False
        if len(stones) == 2:
            return True
        h = {}  # h[k] 是stone k所在的位置
        for i in range(len(stones)):
            h[stones[i]] = i

        dp = [set() for _ in range(len(stones))]
        dp[1].add(1)

        for i in range(1, len(stones)):
            for val in dp[i]:
                if stones[i] + val + 1 in h:
                    dp[h[stones[i] + val + 1]].add(val + 1)
                    if stones[i] + val + 1 == stones[-1]:
                        return True
                if val - 1 > 0 and stones[i] + val - 1 in h:
                    dp[h[stones[i] + val - 1]].add(val - 1)
                    if stones[i] + val - 1 == stones[-1]:
                        return True
                if stones[i] + val in h:
                    dp[h[stones[i] + val]].add(val)
                    if stones[i] + val == stones[-1]:
                        return True
        return False
