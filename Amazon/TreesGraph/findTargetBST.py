# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSumInTree(self, root, target, valMap):
        if not root:
            return False

        if (target - root.val) in valMap:
            return True

        valMap[root.val] = 1

        return self.findSumInTree(root.left, target, valMap) or self.findSumInTree(root.right, target, valMap)

    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        valMap = {}
        return self.findSumInTree(root, target, valMap)