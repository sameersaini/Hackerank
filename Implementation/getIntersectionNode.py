# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # find the lengths of the linked lists
        lenA = 0
        lenB = 0

        tempA = headA
        tempB = headB

        while tempA != None:
            lenA += 1
            tempA = tempA.next

        while tempB != None:
            lenB += 1
            tempB = tempB.next

        # find the diff and move same number of places in the longer list
        # so that now we move equal steps in both the lists
        diff = abs(lenA - lenB)

        tempA = headA
        tempB = headB

        if lenA > lenB:
            temp = headA
            temp2 = headB
        else:
            temp = headB
            temp2 = headA

        while diff > 0:
            temp = temp.next
            diff -= 1

        # move in both lists
        while temp != None:
            if temp == temp2:
                break

            temp = temp.next
            temp2 = temp2.next

        return temp