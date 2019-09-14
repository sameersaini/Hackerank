# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, candidate, paths):
        if not root:
            return

        candidate += str(root.val)
        if not root.left and not root.right:
            paths.append(int(candidate[::], 2))

        self.dfs(root.left, candidate, paths)
        self.dfs(root.right, candidate, paths)

        candidate = candidate[:-1]

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        paths = []

        self.dfs(root, "", paths)

        return sum(paths)
