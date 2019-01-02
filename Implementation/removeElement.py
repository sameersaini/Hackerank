# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        temp = head
        while temp != None and temp.val == val:
            temp = temp.next

        head = temp

        if head == None:
            return head

        if head.next != None:
            prev = head
            temp = head.next

        while temp != None:
            if temp.val == val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev = temp
                temp = temp.next

        return head