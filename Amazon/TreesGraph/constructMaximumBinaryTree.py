"""
The idea is to find the largest value in the array and its corresponding indexes
then call the function recursively with [:index] and [index + 1:] for left and right subtree respectively
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        largest = max(nums)
        index = nums.index(largest)

        head = TreeNode(largest)

        head.left = self.constructMaximumBinaryTree(nums[:index])
        head.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return head