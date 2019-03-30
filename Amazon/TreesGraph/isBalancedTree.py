"""
Algo finds and compare the height of each subtree recursively
and checks if the height diff is more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def compareHeight(self, root, isBalancedFlag):
        if not root:
            return 0

        leftHeight = self.compareHeight(root.left, isBalancedFlag)
        rightHeight = self.compareHeight(root.right, isBalancedFlag)

        if abs(leftHeight - rightHeight) > 1:
            isBalancedFlag[0] = False

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        isBalancedFlag = [True]
        self.compareHeight(root, isBalancedFlag)

        return isBalancedFlag[0]
