# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        nodes = {head.val: 1}
        current = head
        temp = current.next
        while temp != None:
            if temp.val not in nodes:
                nodes[temp.val] = 1
                current.next = temp
                current = temp

            temp = temp.next

        current.next = None

        return head