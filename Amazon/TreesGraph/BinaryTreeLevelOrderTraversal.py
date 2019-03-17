"""
The idea is to do a BFS traversal of the tree by saving [node, level] in the queue
Keep in saving the nodes in a levelValueMap and then return the array level wise.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [[root, 0]]
        levelValueMap = {}

        while len(queue) > 0:
            node, level = queue.pop(0)

            if level + 1 in levelValueMap:
                levelValueMap[level + 1].append(node.val)
            else:
                levelValueMap[level + 1] = [node.val]

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

        return [levelValueMap[key] for key in list(sorted(levelValueMap.keys()))]