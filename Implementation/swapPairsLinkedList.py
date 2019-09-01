# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node1 = head
        node2 = head.next
        node3 = head.next.next

        node2.next = node1

        node1.next = self.swapPairs(node3)

        return node2



