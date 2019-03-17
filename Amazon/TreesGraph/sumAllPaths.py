# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def createNumbers(self, node, number, numbers):
        if not node:
            return

        number = number * 10 + node.val

        if not node.left and not node.right:
            numbers.append(number)

        self.createNumbers(node.left, number, numbers)
        self.createNumbers(node.right, number, numbers)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.right and not root.left:
            return root.val

        initial = root.val
        numbers = []
        self.createNumbers(root.left, initial, numbers)
        self.createNumbers(root.right, initial, numbers)

        return sum(numbers)

