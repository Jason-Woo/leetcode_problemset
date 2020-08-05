# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        list_len = 0
        tmp_node = head
        while tmp_node is not None:
            list_len += 1
            tmp_node = tmp_node.next
        if list_len <= 1:
            return head
        real_k = k % list_len
        if real_k == 0:
            return head
        tmp_node = head
        cnt = 1
        while cnt < list_len - real_k:
            tmp_node = tmp_node.next
            cnt += 1
        new_head = tmp_node.next
        tmp_node.next = None
        tmp_node = new_head
        cnt = 1
        while cnt < real_k:
            tmp_node = tmp_node.next
            cnt += 1
        tmp_node.next = head
        return new_head