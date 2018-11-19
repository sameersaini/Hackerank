#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        newNode = Node(val)
        if self.root == None:
            self.root = newNode
            return

        node = self.root
        while True:
            if val < node.info and node.left == None:
                node.left = newNode
                return
            elif val >= node.info and node.right == None:
                node.right = newNode
                return
            elif val < node.info and node.left != None:
                node = node.left
            else:
                node = node.right


