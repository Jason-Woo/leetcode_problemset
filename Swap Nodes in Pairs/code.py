# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        while curr_node is not None and curr_node.next is not None:
            curr_val = curr_node.val
            curr_node.val = curr_node.next.val
            curr_node.next.val = curr_val
            curr_node = curr_node.next.next
        return head