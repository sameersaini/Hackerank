"""
In a BSt when we delete a node we have to preserve the properties of BST.

To find the node to be deleted call the function recursively by going to left or right sub-tree.

We have to handle 3 cases here for the node to be deleted
    1. Node has no children:
        Return None to the parent
    2. Node has one children:
        if node has left children, then return left else return right to the parent.
    3. Node has 2 children:
        The find the smallest node in the right subtree.
        Copy the value to smallest node in the right subtree to the node to be deleted
        The recursively delete the smallest node in the right subtree

"""

class Solution:
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Solution:
        def findMin(self, node):
            while node.left:
                node = node.left

            return node

        def deleteNode(self, root, key):
            """
            :type root: TreeNode
            :type key: int
            :rtype: TreeNode
            """
            if not root:
                return None

            if root.val == key:
                if not root.left and not root.right:
                    return None
                if not root.left or not root.right:
                    return root.left or root.right

                minNode = self.findMin(root.right)

                root.val = minNode.val

                root.right = self.deleteNode(root.right, minNode.val)

            if root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)

            return root
