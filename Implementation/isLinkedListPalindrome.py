# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(head):
    prev = None
    current = head
    Next = current.next

    while current != None:
        Next = current.next
        current.next = prev
        prev = current
        current = Next

    return prev



class Solution(object):
    def isPalindrome(self, head):
        """
        find the middle of the list and then reverse the second half and then compare the two halves node by node
        """
        if not head or not head.next:
            return True

        slowPtr = head
        fastPtr = head

        while fastPtr != None and fastPtr.next != None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next


        newHead = reverseList(slowPtr)

        temp2 = newHead
        temp1 = head
        while temp2 != None:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        else:
            return True