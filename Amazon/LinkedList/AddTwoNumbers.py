"""
The idea is to sum node by node using simple maths addition and
consider the carry from previous sum of nodes to calculate the sum of current nodes
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = 0
        len2 = 0
        head1 = l1
        head2 = l2

        while l1:
            l1 = l1.next
            len1 += 1

        while l2:
            l2 = l2.next
            len2 += 1

        head = None
        carry = 0
        if head1 and head2:
            value = head1.val + head2.val + carry
            val = (value) % 10
            carry = value // 10
            head = ListNode(val)
            head1 = head1.next
            head2 = head2.next
        elif head1 and not head2:
            head = ListNode(head1.val)
            head1 = head1.next
        elif not head1 and head2:
            head = ListNode(head2.val)
            head2 = head2.next
        else:
            return head

        temp = head
        for _ in range(min(len1, len2) - 1):
            value = head1.val + head2.val + carry
            val = (value) % 10
            carry = value // 10
            node = ListNode(val)

            head1 = head1.next
            head2 = head2.next

            temp.next = node
            temp = node

        if max(len1, len2) == len1 and head1:
            while head1:
                value = head1.val + carry
                val = (value) % 10
                carry = value // 10

                node = ListNode(val)
                temp.next = node
                temp = node

                head1 = head1.next

        elif max(len1, len2) == len2 and head2:
            while head2:
                value = head2.val + carry
                val = (value) % 10
                carry = value // 10

                node = ListNode(val)
                temp.next = node
                temp = node

                head2 = head2.next

        if carry > 0:
            node = ListNode(carry)
            temp.next = node
            temp = node

        temp.next = None

        return head