"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

"""
Take two pointers: slowPtr & fastPtr. intially both are same.
move slowPtr one step
move fastPtr two step

if any pointer reaches a null/None then there is no cycle.
otherwise, due to diffrent speeds, they will match in some iteration, that means there is a cycle.
"""
def has_cycle(head):
    if head == None: return False
    slowPtr = head
    fastPtr = head
    while slowPtr != None or fastPtr != None:
        if fastPtr.next != None:
            fastPtr = fastPtr.next
        else:
            return False

        if fastPtr.data == slowPtr.data:
            return True

        if fastPtr.next != None:
            fastPtr = fastPtr.next
        else:
            return False

        if fastPtr.data == slowPtr.data:
            return True

        if slowPtr.next != None:
            slowPtr = slowPtr.next
        else:
            return False

        if fastPtr.data == slowPtr.data:
            return True
    else:
        return False

