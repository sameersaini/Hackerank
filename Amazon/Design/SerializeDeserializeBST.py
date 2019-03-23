"""
For Serialization:
The idea is to create a string by doing inOrder and preOrder traversal of the tree
For Deserialization:
We can create a BST using the inOrder and preOrder arrays of the tree.
Steps:
1. pop element from start of preOrder array
2. create a tree node from this element
3. find its location in inOrder array and get its index
4. all elements to left will form the left subtree for that node
5. all elements to right will form the right subtree for that node
6. if start > end then return None
7. if start == end then return the tree Node.
8. call the function recursively with the changed boundries for left and right tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def inOrder(self, root, arr):
        if not root:
            return

        self.inOrder(root.left, arr)
        arr.append(root.val)
        self.inOrder(root.right, arr)

    def preOrder(self, root, arr):
        if not root:
            return

        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)

    def findIndex(self, inOrder, val, start, end):
        for i in range(start, end + 1):
            if inOrder[i] == val:
                return i

    def buildTree(self, inOrder, preOrder, start, end):
        if start > end:
            return None

        node = TreeNode(preOrder.pop(0))

        if start == end:
            return node

        index = self.findIndex(inOrder, node.val, start, end)
        node.left = self.buildTree(inOrder, preOrder, start, index - 1)
        node.right = self.buildTree(inOrder, preOrder, index + 1, end)
        return node

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        inOrder = []
        preOrder = []
        self.inOrder(root, inOrder)
        self.preOrder(root, preOrder)

        return "-".join(str(x) for x in inOrder) + ":" + "-".join(str(x) for x in preOrder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        data = data.split(":")
        inOrder = [int(x) for x in data[0].split("-")]
        preOrder = [int(x) for x in data[1].split("-")]

        root = self.buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))