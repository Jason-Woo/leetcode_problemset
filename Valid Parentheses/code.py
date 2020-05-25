class Solution(object): #Atten
    def isValid(self, s):
        left, right, stack = "({[", ")}]", []
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if not stack or left.find(stack.pop()) != right.find(item):
                    return False
        return not stack