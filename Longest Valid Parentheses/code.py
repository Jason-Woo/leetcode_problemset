class Solution(object):
    def longestValidParentheses(self, s):
        # 实际上在找分割点
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        stack = [-1] + stack + [len(s)]
        ans = 0
        for i in range(len(stack)-1):
            ans = max(ans, stack[i+1]-stack[i]-1)
        return ans