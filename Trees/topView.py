"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

"""
hd or horizontal distance is defined as the horizontal distance of a node from the root. nodes on the left side have a -ve distance
and nodes on the right side have a positive distance.
Only one node i.e. the topmost node at a given distance can be part of the top view.
So, Do a BFS and maintain a map to store topmost node at every horizontal distance. if a node at a particulat hd has been seen once
other nodes at that distance will be rejected.
"""
def topView(root):
    #Write your code here
    queue = [[root, 0]]
    hdMap = {}

    while len(queue) != 0:
        node, hd = queue[0]
        queue.pop(0)
        if hd not in hdMap:
            hdMap[hd] = node.info

        if node.left != None:
            queue.append([node.left, hd - 1])
        if node.right != None:
            queue.append([node.right, hd + 1])

    for hd in sorted(list(hdMap.keys())):
        print(hdMap[hd], end=' ')
