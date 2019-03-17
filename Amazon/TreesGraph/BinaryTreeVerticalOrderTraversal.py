"""
The idea is to do a BFS traversal of the tree by saving [node, column] in the queue
While saving, decrease the column by 1 for left node and increase the column by 1 for right node
Keep in saving the nodes in a columnValueMap and then return the array column wise.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        columnValueMap = {0: [root.val]}
        queue = [[root, 0]]

        while len(queue) > 0:
            node, column = queue.pop(0)

            if node.left:
                queue.append([node.left, column - 1])
                if column - 1 in columnValueMap:
                    columnValueMap[column - 1].append(node.left.val)
                else:
                    columnValueMap[column - 1] = [node.left.val]

            if node.right:
                queue.append([node.right, column + 1])
                if column + 1 in columnValueMap:
                    columnValueMap[column + 1].append(node.right.val)
                else:
                    columnValueMap[column + 1] = [node.right.val]

        return [columnValueMap[key] for key in list(sorted(columnValueMap.keys()))]
