# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    head = None

    def findSize(self, head):
        length = 0
        while head:
            length += 1
            head = head.next

        return length

    def createTree(self, left, right):

        if right < left:
            return None

        mid = (left + right) // 2
        lNode = self.createTree(left, mid - 1)

        root = TreeNode(self.head.val)
        root.left = lNode

        self.head = self.head.next
        root.right = self.createTree(mid + 1, right)

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        self.head = head
        size = self.findSize(head)

        return self.createTree(0, size - 1)