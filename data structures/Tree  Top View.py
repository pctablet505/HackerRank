"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from queue import Queue


def topView(root):
    uniq_lvls = []
    q = Queue()
    q.put((root, 0))

    while not q.empty():
        temp = q.get()
        if temp[1] not in (i[1] for i in uniq_lvls):
            uniq_lvls.append(temp)
        if temp[0].left:
            q.put((temp[0].left, temp[1] - 1))
        if temp[0].right:
            q.put((temp[0].right, temp[1] + 1))
    for x in sorted(uniq_lvls, key=lambda e: e[1]):
        print(x[0].info, end=' ')
