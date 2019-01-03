# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def checkSymmetric(right, left):
    if not right and not left:
        return True

    if not right or not left:
        return False

    return right.val == left.val and checkSymmetric(right.right, left.left) and checkSymmetric(right.left, left.right)


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        else:
            return checkSymmetric(root.right, root.left)