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