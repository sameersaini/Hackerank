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
    def createTree(self, arr, left, right):
        if right < left:
            return None

        mid = (left + right) // 2

        root = TreeNode(arr[mid])

        root.left = self.createTree(arr, left, mid - 1)
        root.right = self.createTree(arr, mid + 1, right)

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        root = self.createTree(arr, 0, len(arr) - 1)

        return root
