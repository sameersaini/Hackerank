# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        The logic is that a node is non duplicate if its value is not equal the its next or previous node.
        """
        if not head: return head

        current = head
        previous = None

        # for finding the head in case of duplicates at the start of the list
        while current != None and ((previous != None and current.val == previous.val) or (current.next != None and current.val == current.next.val)) :
            previous = current
            current = current.next

        previous = current
        head = previous

        if not head:
            return head

        """
        remove duplicates from the list by using 3 pointers
        current is the current location
        previous is the pointer that maintains the actual list
        temp is temporary pointer to keep track of duplicate node.

        In case of duplicate nodes, temp keeps the track of prevous duplicate node
        When a non duplicate node is found we set previous of next to the current node.
        """
        current = current.next
        temp = previous
        while current != None:
            if (current.val != temp.val) and (current.next == None or current.val != current.next.val):
                previous.next=current
                previous = current
                temp = previous

            temp = current
            current = current.next

        previous.next=current
        return head