# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

def insert(self, val):
    if self.root == None:
        self.root = Node(val)
        return
    root = self.root
    while True:
        if val > root.info:
            if root.right is None:
                root.right = Node(val)
                break
            else:
                root = root.right
        if val < root.info:
            if root.left is None:
                root.left = Node(val)
                break
            else:
                root = root.left
