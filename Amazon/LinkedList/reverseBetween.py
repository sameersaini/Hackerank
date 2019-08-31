# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head

        prev = None
        curr = head

        for i in range(m - 1):
            prev = curr
            curr = curr.next

        first = prev
        second = curr

        for _ in range(m, n + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        if first:
            first.next = prev
            second.next = curr
        else:
            second.next = curr
            head = prev

        return head


