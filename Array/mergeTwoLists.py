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

        while temp1 != None:
            arr1.append(temp1.val)
            temp1 = temp1.next

        while temp2 != None:
            arr1.append(temp2.val)
            temp2 = temp2.next

        newArr = sorted(arr1)

        if len(newArr) == 0:
            return None

        newList = ListNode(newArr[0])
        temp = newList

        for val in newArr[1:]:
            node = ListNode(val)
            temp.next = node
            temp = node

        return newList