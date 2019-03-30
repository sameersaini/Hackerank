# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSums(self, node, sum, total, arr, currentArr):
        if not node.left and not node.right:
            if (total + node.val) == sum:
                currentArr.append(node.val)
                arr.append(currentArr)
            return

        temp = currentArr[::]
        temp.append(node.val)

        if not node.right:
            self.checkSums(node.left, sum, total + node.val, arr, temp)
        elif not node.left:
            self.checkSums(node.right, sum, total + node.val, arr, temp)
        else:
            tempLeft, tempRight = currentArr[::], currentArr[::]
            tempLeft.append(node.val)
            tempRight.append(node.val)
            self.checkSums(node.left, sum, total + node.val, arr, tempLeft)
            self.checkSums(node.right, sum, total + node.val, arr, tempRight)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        arr = []

        if not root:
            return arr

        self.checkSums(root, sum, 0, arr, [])
        return arr
