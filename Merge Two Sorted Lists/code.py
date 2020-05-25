# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None: #Atten
            if l1 is None: return l2
            else: return l1
        iter1, iter2 = l1, l2
        if l1.val < l2.val:
            head = ListNode(l1.val, None)
            iter1 = l1.next
        else:
            head = ListNode(l2.val, None)
            iter2 = l2.next
        curr_node = head
        while iter1 is not None or iter2 is not None:
            if iter1 is None:
                tmp_node = ListNode(iter2.val, None)
                iter2 = iter2.next
            elif iter2 is None:
                tmp_node = ListNode(iter1.val, None)
                iter1 = iter1.next
            else:
                if iter1.val < iter2.val:
                    tmp_node = ListNode(iter1.val, None)
                    iter1 = iter1.next
                else:
                    tmp_node = ListNode(iter2.val, None)
                    iter2 = iter2.next
            curr_node.next = tmp_node
            curr_node = tmp_node
        return head