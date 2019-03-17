"""
The idea is to check if the left node of left tree is equal to right node of right tree
and if the right node of left tree is equal to left node of right tree
While comparing,
if both nodes are None then return True and if any node is None then return False for those two nodes
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right,
                                                                                                             right.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.checkSymmetric(root.left, root.right)
