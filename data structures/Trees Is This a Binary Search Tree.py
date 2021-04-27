""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkBST(root):    
    inorder=[]
    def ino(root):
        if root:
            ino(root.left)
            inorder.append(root.data)
            ino(root.right)
    ino(root)
    return inorder==sorted(set(inorder))
        