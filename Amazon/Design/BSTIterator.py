"""
To get the next value in a BST, we cannot move to the left side.
The next value is always be the parent node or the smallest right child.

Therefore, To create an iterator which returns the next increasing value in the BST,
we need to store the back pointers to all the left nodes in a stack.

For hasNext, return true if the size of stack > 0
For next,
    Pop the mode from stack.
    Push its right node and all its left nodes to the stack
    return the value at poped node

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodeStack = []
        self.pushToStack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.nodeStack.pop()
        self.pushToStack(node.right)

        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.nodeStack) != 0

    def pushToStack(self, node):
        if node:
            self.nodeStack.append(node)
            self.pushToStack(node.left)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()