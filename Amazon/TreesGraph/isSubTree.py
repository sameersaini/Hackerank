"""
The idea is to find the root of small tree in the main tree
and then check if subtree in main tree is same as the small tree
Iteratively, check for all the matches in the main tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def matchTrees(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        return node1.val == node2.val and self.matchTrees(node1.right, node2.right) and self.matchTrees(node1.left,
                                                                                                        node2.left)

    def matchNode(self, node, target):
        if not node:
            return False

        if node.val == target.val:
            if self.matchTrees(node, target):
                return True

        return self.matchNode(node.left, target) or self.matchNode(node.right, target)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True

        if not s or not t:
            return False

        return self.matchNode(s, t)
