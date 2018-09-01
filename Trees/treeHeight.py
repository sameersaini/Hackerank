def height(root):
    if root == None or (root.left == None and root.right == None):
        return 0
    return max([height(root.left), height(root.right)]) + 1