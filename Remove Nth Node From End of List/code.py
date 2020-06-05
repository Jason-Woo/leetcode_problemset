# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def iter_list(self, node, n):
        curr_level = 0
        if node.next is None:
            curr_level = 1
            next_node = None
        else:
            next_level, next_node = self.iter_list(node.next, n)
            curr_level = next_level + 1
        if curr_level == n:
            curr_node = node.next
        else:
            curr_node = ListNode(node.val, next_node)
        return curr_level, curr_node



    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        _, n_head = self.iter_list(head, n)
        return n_head
