# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # find length of the list
        if head == None:
            return head

        # find the length of the list
        length = 0
        temp = head

        while temp != None:
            temp = temp.next
            length += 1


        # find the actual shifts required
        actualShits = k % length
        jumps = length - actualShits

        # go to the rotation node
        temp = head
        while jumps != 1:
            temp = temp.next
            jumps -= 1

        #fetch the new head
        newHead = temp.next
        temp.next = None

        # boundry checking
        if newHead == None:
            return head

        # iterate to the end of the sublist
        temp = newHead
        while temp.next != None: temp = temp.next

        # move the sublist to the start and return the head of new list
        temp.next = head
        head = newHead

        return head