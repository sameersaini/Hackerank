# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        str1 = ''
        str2 = ''

        temp1 = l1
        temp2 = l2

        while temp1:
            str1 += str(temp1.val)
            temp1 = temp1.next

        while temp2:
            str2 += str(temp2.val)
            temp2 = temp2.next

        ans = str(int(str1) + int(str2))

        head = ListNode(ans[0])
        temp = head
        for c in ans[1:]:
            node = ListNode(c)
            temp.next = node
            temp = node

        return head