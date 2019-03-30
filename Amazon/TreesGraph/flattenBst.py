"""
Do a DFS using a stack and save a pointer to previous Node.
Save current node as right node of the previous node and mark left node of previous node as Null
i.e.
prev->right = curr
prev->left = None

prev = curr
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, stack):
        prev = None
        while len(stack) > 0:
            curr = stack.pop()

            if curr.right:
                rightNode = curr.right
                stack.append(rightNode)

            if curr.left:
                leftNode = curr.left
                stack.append(leftNode)

            if prev:
                prev.right = curr
                prev.left = None

            prev = curr

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.levelOrder([root])
