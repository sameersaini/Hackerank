"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def levelOrderTraversal(self, root, levelMap, level):
        if not root:
            return

        if level in levelMap:
            levelMap[level].append(root)
        else:
            levelMap[level] = [root]

        self.levelOrderTraversal(root.left, levelMap, level + 1)
        self.levelOrderTraversal(root.right, levelMap, level + 1)

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        levelMap = {}

        self.levelOrderTraversal(root, levelMap, 0)

        for level in levelMap:
            nodesArr = levelMap[level]
            for i in range(len(nodesArr) - 1):
                nodesArr[i].next = nodesArr[i + 1]

        return root
