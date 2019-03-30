# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkPathSum(self, node, total, sum):
        if not node.left and not node.right:
            if (total + node.val) == sum:
                return True
            else:
                return False

        if not node.right:
            return self.checkPathSum(node.left, total + node.val, sum)

        if not node.left:
            return self.checkPathSum(node.right, total + node.val, sum)

        return self.checkPathSum(node.left, total + node.val, sum) or self.checkPathSum(node.right, total + node.val,
                                                                                        sum)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        return self.checkPathSum(root, 0, sum)
