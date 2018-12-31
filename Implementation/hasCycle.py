# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # user 2 pointers. move slow by one step and fast by 2 step
        # if there is a cycle, then they will meet at sometime in future
        # else, fast pointer will reach end of list.
        slowPtr = head
        fastPtr = head

        while True:
            if slowPtr == None or fastPtr == None:
                return False

            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

            if fastPtr != None:
                fastPtr = fastPtr.next
            else:
                return False

            if slowPtr == fastPtr:
                return True
