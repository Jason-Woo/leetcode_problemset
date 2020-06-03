# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = ListNode(-1, None)
        curr_node2 = new_head
        curr_node = head
        while curr_node is not None:
            cnt = 0
            stack = []
            while cnt < k and curr_node is not None:
                stack.append(curr_node)
                curr_node = curr_node.next
                cnt += 1
            if cnt == k:
                while stack:
                    tmp_node = stack.pop()
                    curr_node2.next = tmp_node
                    curr_node2 = curr_node2.next
            else:
                while stack:
                    tmp_node = stack.pop(0)
                    curr_node2.next = tmp_node
                    curr_node2 = curr_node2.next
        curr_node2.next = None #Atten
        return new_head.next