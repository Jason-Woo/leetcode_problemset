class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_size = 0 #Atten
        for i in range(len(s)):
            ele = [s[i]]
            size = 1
            for j in range(i + 1, len(s)):
                if s[j] not in ele:
                    ele.append(s[j])
                    size += 1
                else:
                    break
            if size > max_size:
                max_size = size
        return max_size

s=Solution
print(s.lengthOfLongestSubstring(s,''))