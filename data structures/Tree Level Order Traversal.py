

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    from queue import Queue
    current=root
    q=Queue()
    q.put_nowait(current)
    s=''
    while not q.empty():
        current=q.get()
        s+=str(current.info)+' '
        if current.left:
            q.put_nowait(current.left)
        if current.right:
            q.put_nowait(current.right)
    print(s)

