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
        if head == None:
            return None

        if head.next == None:
            return head

        temp1 = head
        temp2 = temp1.next

        temp1.next = temp2.next
        temp2.next = temp1

        head = temp2

        current = temp1

        if current.next == None:
            return head
        else:
            temp1 = current.next

        if temp1.next == None:
            return head
        else:
            temp2 = temp1.next


        while current.next != None:
            temp1.next = temp2.next
            temp2.next = temp1
            current.next = temp2

            current = temp1

            if current.next == None:
                return head
            else:
                temp1 = current.next

            if temp1.next == None:
                return head
            else:
                temp2 = temp1.next



