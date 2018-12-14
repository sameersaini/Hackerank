# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        table = {}

        node = head
        counter = 0
        while node != None:
            counter += 1
            table[counter] = node
            node = node.next

        prevNodeNumber = counter - n
        nextNodeNumber = counter - n + 2

        if n == counter:
            if counter > 1:
                head = table[2]
            else:
                head = None
        elif n == 1:
            table[prevNodeNumber].next = None
        else:
            table[prevNodeNumber].next = table[nextNodeNumber]

        return head
