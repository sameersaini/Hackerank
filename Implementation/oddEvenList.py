# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        evenHead = head.next

        tempOdd = head
        tempEven = head.next

        while tempEven and tempEven.next:
            tempOdd.next = tempEven.next
            tempEven.next = tempOdd.next.next

            tempOdd = tempOdd.next
            tempEven = tempEven.next

        tempOdd.next = evenHead

        return head
