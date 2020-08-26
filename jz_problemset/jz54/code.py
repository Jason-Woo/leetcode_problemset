# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.dict = {}
        self.queue = []

    def FirstAppearingOnce(self):
        # write code here
        for char in self.queue:
            if self.dict[char] == 1:
                return char
        return '#'

    def Insert(self, char):
        # write code here
        self.queue.append(char)
        if char in self.dict.keys():
            self.dict[char] += 1
        else:
            self.dict[char] = 1