# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        arr1 = []
        arr2 = []

        temp1 = l1
        temp2 = l2

        if l1 != None:
            if l2 != None and l2.val <= l1.val:
                newList = ListNode(l2.val)
                l2 = l2.next
            else:
                newList = ListNode(l1.val)
                l1 = l1.next
        else:
            if l2 != None:
                newList = ListNode(l2.val)
                l2 = l2.next
            else:
                return None

        temp = newList
        while l1 != None or l2 != None:
            node = None
            if l1 != None:
                if l2 != None and l2.val <= l1.val:
                    node = ListNode(l2.val)
                    l2 = l2.next
                else:
                    node = ListNode(l1.val)
                    l1 = l1.next
            else:
                if l2 != None:
                    node = ListNode(l2.val)
                    l2 = l2.next
            if node != None:
                temp.next = node
                temp = node

        return newList