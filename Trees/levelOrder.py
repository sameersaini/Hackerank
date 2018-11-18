"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
Do a BFS
"""
def levelOrder(root):
    #Write your code here
    queue = [root]

    while len(queue) != 0:
        node = queue[0]
        queue.pop(0)
        print(node.info, end=' ')

        if node.left != None: queue.append(node.left)
        if node.right != None: queue.append(node.right)