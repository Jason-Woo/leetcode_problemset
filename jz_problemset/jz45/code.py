# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        cards = [0 for _ in range(14)]
        for card in numbers:
            cards[card] += 1
        p, cnt = 1, len(numbers) - cards[0]
        while p < 14 and cards[p] == 0:
            p += 1
        while p < 14 and cnt > 0:
            if cards[p] == 0:
                cards[0] -= 1
                if cards[0] < 0:
                    return False
                p += 1
            elif cards[p] == 1:
                p += 1
                cnt -= 1
            else:
                return False
        return True