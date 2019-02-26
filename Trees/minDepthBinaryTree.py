# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.right and not root.left:
            return 1

        if not root.right:
            return 1 + self.minDepth(root.left)

        if not root.left:
            return 1 + self.minDepth(root.right)

        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
