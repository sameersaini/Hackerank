# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # keep on copying value from next node to the current node till the end of the list
        # this only works if we are not given last node of the list
        # after loop is complete, set the next of second last node to None, coz we have delete one node from the list and copied all the other values one node up, so last node is not required.
        while node.next != None:
            previous = node
            node.val = node.next.val
            node = node.next

        previous.next = None