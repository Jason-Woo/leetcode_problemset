class Solution(object):
    def dfs(self, candidates, target, path, result, idx):
        if target == 0:
            result.append(path)
            return
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            if target >= candidates[i]:
                self.dfs(candidates, target - candidates[i], path + [candidates[i]], result, i + 1) #usage of i

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.dfs(candidates, target, [], result, 0)
        return result