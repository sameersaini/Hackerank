"""
The idea is to create an extra node x' between every two nodes x and y
For example:
    1->1'->2->2'->3->3'->None

x is the original node and x' is the copy node
For every pair of original and copy node:
    copy->random = original->random->next
This points the random pointer in every copy node to correct copy node
Now, we need to separate original and copy lists

For every pair of original and copy node:
    original->next = original->next->next
    copy->next = copy->next->next

Finally return the pointer to copyHead
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        node = head
        while node:
            copy = Node(node.val, None, None)

            temp = node.next
            node.next = copy
            copy.next = temp

            node = temp

        original = head
        while original:
            copy = original.next
            if original.random:
                copy.random = original.random.next

            original = original.next.next

        original = head
        copyHead = original.next
        copy = original.next

        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next

            original = original.next
            copy = copy.next

        return copyHead