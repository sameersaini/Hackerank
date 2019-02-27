# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = [[root, 0]]
        valueHeightMap = {}

        while len(queue) > 0:
            node, height = queue.pop(0)
            if height in valueHeightMap:
                valueHeightMap[height].append(node.val)
            else:
                valueHeightMap[height] = [node.val]

            if node.left:
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])

        ans = []
        for keys in sorted(list(valueHeightMap.keys())):
            ans.append(valueHeightMap[keys][-1])

        return ans
