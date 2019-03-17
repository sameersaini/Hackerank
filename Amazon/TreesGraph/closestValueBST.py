# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMin(self, node, minNode, minDiff, target):
        if not node:
            return

        nodeDiff = abs(node.val - target)
        if nodeDiff < minDiff:
            minDiff = nodeDiff
            minNode[0] = node.val

        self.findMin(node.right, minNode, minDiff, target)
        self.findMin(node.left, minNode, minDiff, target)

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        minNode = [root.val]
        minDiff = abs(root.val - target)

        self.findMin(root, minNode, minDiff, target)

        return minNode[0]
