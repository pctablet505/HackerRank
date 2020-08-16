'''there is problem in hackerrank timeout settings'''
'''The same algorithm works in java and c++'''
'''please see java code'''


import sys
from sys import stdin, stdout

sys.setrecursionlimit(99999999)
from random import randint


def rand():
    return randint(1, 2 ** 64)


class Node:
    def __init__(self, key, priority, size=1):
        self.priority = priority
        self.key = key
        self.left = None
        self.right = None
        self.size = size
        self.rev = False


def size(item):
    if item:
        return item.size
    return 0


def update_count(node):
    if node:
        node.size = size(node.left) + size(node.right) + 1


def push(node):
    if node and node.rev:
        node.rev = False
        node.left, node.right = node.right, node.left
        if node.left:
            node.left.rev ^= True
        if node.right:
            node.right.rev ^= True


def merge(l, r):
    push(l)
    push(r)
    if not l:
        return r
    if not r:
        return l
    elif l.priority > r.priority:
        l.right = merge(l.right, r)
        t = l
    else:
        r.left = merge(l, r.left)
        t = r
    update_count(t)
    return t


def getValue(t, key, add=0):
    push(t)
    cur_key = add + size(t.left)
    if key == cur_key:
        return t.key
    if key < cur_key:
        return getValue(t.left, key, add)
    else:
        return getValue(t.right, key, add + 1 + size(t.left))


def split(t, key, add=0):
    if not t:
        return (None, None)
    push(t)
    curr_key = add + size(t.left)
    if key <= curr_key:
        l, t.left = split(t.left, key, add)
        r = t
    else:
        t.right, r = split(t.right, key, add + 1 + size(t.left))
        l = t
    update_count(t)
    return (l, r)


def reverse(t, l, r):
    t1, t2 = split(t, l)
    t2, t3 = split(t2, r - l + 1)
    t2.rev ^= True
    t = merge(t1, t2)
    t = merge(t, t3)
    return t


def insert(t, index, value):
    t1, t2 = split(t, index)
    t = merge(t1, Node(value, rand()))
    t = merge(t, t2)
    return t


def kth(root, k):
    push(root)
    if k < size(root.left):
        return kth(root.left, k)
    elif k > size(root.left):
        return kth(root.right, k - size(root.left) - 1)
    return root.key


def traverse(root):
    global pos
    global snapshot
    if not root:
        return
    push(root)
    traverse(root.left)
    snapshot[pos] = root.key
    pos += 1
    traverse(root.right)


n, q = map(int, stdin.readline().split())
root = None
snapshot = [0] * n
inv = [0] * n
for i in range(n):
    root = insert(root, i, i)
    inv[i] = i
M = 300
left = [0] * M
right = [0] * M
count = 0
s = ''
for i in range(q):
    query = list(map(int, stdin.readline().split()))
    type = query[0]
    if type == 1:
        a = query[1] - 1
        b = query[2] - 1
        root = reverse(root, a, b)
        left[count] = a
        right[count] = b
        count += 1
        if count == M:
            pos = 0
            traverse(root)
            for j in range(n):
                inv[snapshot[j]] = j
            count = 0
    elif type == 2:
        x = query[1] - 1
        cur = inv[x]
        for j in range(count):
            if left[j] <= cur and cur <= right[j]:
                cur = left[j] + right[j] - cur

        s += 'element {} is at position {}\n'.format(x + 1, cur + 1)
    else:
        y = query[1] - 1
        s += 'element at position {} is {}\n'.format(y + 1, kth(root, y) + 1)
stdout.write(s)
