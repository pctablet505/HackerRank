

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    if root:
        print(str(root),end=' ')
        preOrder(root.left)
        preOrder(root.right)
