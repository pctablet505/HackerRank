import os, sys


class BITNode:
    __slots__ = ['x', 'p', 'px', 'c']

    def __init__(self, x=0, p=0, px=0, c=0):
        self.x = x
        self.p = p
        self.px = px
        self.c = c

    def __iadd__(self, other):
        self.x += other.x
        self.p += other.p
        self.px += other.px
        self.c += other.c
        return self

    def __radd__(self, other):
        return BITNode(self.x, self.p, self.px, self.c)

    def __sub__(self, other):
        return BITNode(self.x - other.x, self.p - other.p, self.px - other.px, self.c - other.c)


def getSum(BITTree, i):
    s = 0
    while i:
        s += BITTree[i - 1]
        i -= i & (-i)
    return s


def getRangeSum(BITTree, i, j):
    return getSum(BITTree, j) - getSum(BITTree, i)


def addBIT(BITTree, i, v):
    i += 1
    bound = len(BITTree) + 1
    while i < bound:
        BITTree[i - 1] += v
        i += i & (-i)


p_limit = 10 ** 4 + 1
bitTree = [BITNode() for i in range(p_limit)]


def solve(X, P):
    cities = sorted(zip(X, P))
    cable = 0
    for x, p in cities:
        underP = getSum(bitTree, p)
        overP = getRangeSum(bitTree, p, p_limit)
        cable += (p * (underP.c * x - underP.x) + (overP.p * x - overP.px))
        addBIT(bitTree, p, BITNode(x, p, x * p, 1))
    for f in bitTree:
        f.__init__()
    return cable % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))
        populations = list(map(int, input().rstrip().split()))

        result = solve(arr, populations)

        fptr.write(str(result) + '\n')

    fptr.close()
