"""
The idea is that the inOrder traversal of a valid BST return a sorted array.
So, if the array is sorted, the the tree is valid, else invalid
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self, root, nodes):
        if not root:
            return
        self.inOrder(root.left, nodes)
        nodes.append(root.val)
        self.inOrder(root.right, nodes)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        nodes = []
        self.inOrder(root, nodes)

        for i in range(1, len(nodes)):
            if nodes[i] <= nodes[i - 1]:
                return False

        return True