# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ''
        num = 0
        while (l1 is not None and l2 is not None) or num != 0: #atten
            if l1 is not None:
                num += l1.val
                l1 = l1.next
            if l2 is not None:
                num += l2.val
                l2 = l2.next
            if num >= 10:
                result += str(num-10)
                num = 1
            else:
                result += str(num)
                num = 0
        result = result[::-1]
        p = ListNode(int(result[0]),None)
        for i in range(1, len(result)):
            tmp_node = ListNode(int(result[i]),p)
            p = tmp_node
        return p


