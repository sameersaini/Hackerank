# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inOrder(node, arr):
    if node == None:
        return

    inOrder(node.left, arr)
    arr.append(node.val)
    inOrder(node.right, arr)


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        inOrder(root, ans)

        return ans