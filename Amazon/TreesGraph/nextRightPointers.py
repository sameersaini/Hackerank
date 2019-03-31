"""
This works only for a complete binary tree.
We do a modified pre order traversal and set next of node's left child to node's right child
and
set next of node's right child to left node of node's next node.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        if root.left:
            root.left.next = root.right

        if root.next and root.right:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
