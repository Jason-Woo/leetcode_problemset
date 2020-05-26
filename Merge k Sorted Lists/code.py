# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        else:
            mid = len(lists) // 2
            l1 = self.mergeKLists(lists[0:mid])
            l2 = self.mergeKLists(lists[mid:])
            head = ListNode(-1, None)
            curr_node = head
            while l1 is not None or l2 is not None:
                if l1 is None:
                    curr_node.next = l2
                    break
                elif l2 is None:
                    curr_node.next = l1
                    break
                if l1.val < l2.val:
                    tmp_node = ListNode(l1.val, None)
                    l1 = l1.next
                else:
                    tmp_node = ListNode(l2.val, None)
                    l2 = l2.next
                curr_node.next = tmp_node
                curr_node = tmp_node
            return head.next
