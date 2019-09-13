# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def createBst(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) // 2

        root = TreeNode(nums[mid])
        root.left = self.createBst(nums, left, mid - 1)
        root.right = self.createBst(nums, mid + 1, right)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        return self.createBst(nums, 0, len(nums) - 1)
