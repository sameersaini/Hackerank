"""
The idea is to find the length of both the linked list
Find the larger linked list and move forward in it by difference of the length between larger and smaller list
After this, move one step forward in both the lists and keep on checking for intersection
If intersection is there then return the node else return None
"""

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
        if not headA or not headB:
            return None

        len1 = 0
        len2 = 0
        tempA = headA
        tempB = headB

        while tempA:
            len1 += 1
            tempA = tempA.next

        while tempB:
            len2 += 1
            tempB = tempB.next

        longer = max(len1, len2)
        abs_diff = abs(len1 - len2)
        if longer == len1:
            for _ in range(abs_diff):
                headA = headA.next
        else:
            for _ in range(abs_diff):
                headB = headB.next

        for _ in range(longer - abs_diff):
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
