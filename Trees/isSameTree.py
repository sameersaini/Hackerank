# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def checkSame(p,q):
    if p == None and q == None:
        return True
    elif (p == None and q != None) or (p != None and q == None):
        return False
    else:
        return (p.val == q.val) and checkSame(p.left,q.left) and checkSame(p.right,q.right)


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return checkSame(p, q)