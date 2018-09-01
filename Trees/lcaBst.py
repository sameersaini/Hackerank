"""
First find the path to both the nodes and the traverse both the paths for the last common node.
That node will be the least common ancestor of both the nodes.
"""
def path(node, value, arr):
    # base case
    if node == None: return False

    # append to the node to the path
    arr.append(node)

    # if node is found then return True.
    if node.info == value: return True

    # if node is found in left or right sub tree, then return True
    if (node.left != None and path(node.left, value, arr)) or ( node.right != None and path(node.right, value, arr)):
        return True

    # if node is not found in the either left or right sub tree, the pop the pushed node and return false.
    arr.pop()
    return False



def lca(root, v1, v2):
    # lists to hold the paths to node values v1 and v2.
    arr1, arr2 = [], []
    v1Path = path(root, v1, arr1)
    v2Path = path(root, v2, arr2)

    # array traverse logic to find the LCA
    minimum = min([len(arr1), len(arr2)])
    for i in range(minimum):
        node1 = arr1[i]
        node2 = arr2[i]
        if node1.info == node2.info:
            common = node1
        else:
            break
    return common