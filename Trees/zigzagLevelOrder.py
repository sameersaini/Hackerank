# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        q = [[root, 0]]

        valueDepthMap = {}
        length = 0

        while len(q) != 0:
            node, height = q.pop(0)
            if height in valueDepthMap:
                valueDepthMap[height].append(node.val)
            else:
                valueDepthMap[height] = [node.val]

            if node.left:
                q.append([node.left, height + 1])

            if node.right:
                q.append([node.right, height + 1])

        ans = []
        for key in sorted(list(valueDepthMap.keys())):
            if key % 2 == 0:
                toAppend = valueDepthMap[key]
            else:
                toAppend = valueDepthMap[key][::-1]

            ans.append(toAppend)

        return ans
