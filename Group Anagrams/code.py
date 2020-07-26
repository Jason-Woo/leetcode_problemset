class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        hash_tbl = []
        for s in strs:
            hash_str = sorted(s)
            if hash_str in hash_tbl:
                ans[hash_tbl.index(hash_str)].append(s)
            else:
                hash_tbl.append(hash_str)
                ans.append([s])
        return ans

# class Solution(object): #Use dict!!
#     def groupAnagrams(self, strs):
#         d = {}
#         for string in strs:
#             s = "".join(sorted(string))
#             d[s] = d.get(s, []) + [string]
#         return [l for l in d.values()]