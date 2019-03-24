"""
The idea is utilize the properties of BST.
let p be small node and q be larger or adjust accordingly.
If the node is between p and q, then return it
If both nodes are smaller than the root, then call with left node.
else, call with right node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p.val > q.val:
            p, q = q, p

        if (p.val < root.val < q.val) or p.val == root.val or q.val == root.val:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
