# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        else:
            root = sequence[-1]
            mid = 0
            while sequence[mid] < root:
                mid += 1
            left_seq = sequence[:mid]
            right_seq = sequence[mid:-2]
            for i in range(mid, len(sequence) - 1):
                if sequence[i] < root:
                    return False
            ans = True
            if len(left_seq) >= 1:
                ans = ans and self.VerifySquenceOfBST(left_seq)
            if len(right_seq) >= 1:
                ans = ans and self.VerifySquenceOfBST(right_seq)
            return ans
