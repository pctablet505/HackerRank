"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    if root:
        print(root.info, end=' ')
        topView(root.right)
