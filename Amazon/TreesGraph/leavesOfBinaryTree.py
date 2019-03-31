"""
The idea is to move in a DFS way to find the height of the Tree in a bottom up manner.
For every node, save its val corresponding to its height from bottom in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getLeaves(self, node, arr):
        if not node:
            return -1

        currentHeight = 1 + max(self.getLeaves(node.left, arr), self.getLeaves(node.right, arr))

        if len(arr) > currentHeight:
            arr[currentHeight].append(node.val)
        else:
            arr.append([node.val])

        return currentHeight

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        arr = []
        self.getLeaves(root, arr)
        return arr