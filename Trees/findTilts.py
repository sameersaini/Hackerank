# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSums(self, root, tilts):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        rightVal = self.findSums(root.right, tilts)
        leftVal = self.findSums(root.left, tilts)

        tilts.append(abs(rightVal - leftVal))

        return rightVal + leftVal + root.val

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        tilts = []
        self.findSums(root, tilts)

        return sum(tilts)
