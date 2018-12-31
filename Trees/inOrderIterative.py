# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        push root onto stack & then keep on pushing the left node onto stack till left node is not None
        if left node is None and stack is not empty then pop the top of stack and append it in a arr.
        then set the right node as the current node. and repeat the loop till the left is None and stack is not empty.
        """



        ans = []
        stack = []

        current = root

        while True:
            while current != None:
                stack.append(current)
                current = current.left

            if len(stack) != 0:
                current = stack.pop()
                ans.append(current.val)

                current = current.right
            else:
                break

        return ans