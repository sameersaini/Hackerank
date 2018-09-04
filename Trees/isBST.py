"""
In order traversal of an actual BST returns an array, which is sorted in Ascending order.
If the returned array is not sorted in ascending order, then the tree is not BST.
"""

def iorder(root, arr):
    if root == None:
        return True
    iorder(root.left, arr)
    arr.append(root.data)
    iorder(root.right, arr)
    return arr

def checkBST(root):
    arr = iorder(root, [])
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            return False
    return True