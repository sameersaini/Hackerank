# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # user 2 pointers. move slow by one step and fast by 2 step
        # if there is a cycle, then they will meet at sometime in future
        # else, fast pointer will reach end of list.

        slowPtr = head
        fastPtr = head

        while True:
            if slowPtr == None or fastPtr == None:
                return None

            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

            if fastPtr != None:
                fastPtr = fastPtr.next
            else:
                return None

            if slowPtr == fastPtr:
                break

        # when a loop exits, then reset slowPtr to head and then move slow and fast pointer by one step.
        # the first node they meet is the node where the loop starts
        slowPtr = head

        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        return slowPtr