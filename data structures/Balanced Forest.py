from collections import defaultdict
from collections import deque
from math import ceil, log2


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = dict()
        self.subtree_weights = dict()
        self.parents = defaultdict(list)
        self.depth = defaultdict(int)
        self.sums = defaultdict(list)
        self.enter = defaultdict(int)
        self.exit = defaultdict(int)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, start=None):
        stack = []
        visited = set()
        if not start:
            current = next(iter(self.graph))
        else:
            current = start
        visited.add(current)
        stack.append(current)
        while len(stack) > 0:
            v = stack.pop()

            print(v)
            for x in self.graph[v]:
                if x not in visited:
                    stack.append(x)
                    visited.add(x)

    def getPath(self, start, end):
        if start == end:
            return [start]

        def util(parent, end):

            curr = end
            path = [end]
            while curr in parent:
                path.append(parent[curr])
                curr = parent[curr]
            return path

        visited = set()
        q = deque()
        q.appendleft(start)
        visited.add(start)
        parent = {}
        while len(q):
            v = q.pop()
            for x in self.graph[v]:
                if x not in visited:
                    parent[x] = v
                    q.appendleft(x)
                    visited.add(x)
                    if x == end:
                        return util(parent, end)

    def longestPahInTree(self):
        start = next(iter(self.graph))

        def util(self, start):
            farthest = start
            visited = set()
            q = deque()
            q.appendleft(start)
            visited.add(start)
            while len(q):
                v = q.pop()

                for x in self.graph[v]:
                    if x not in visited:
                        farthest = x
                        q.appendleft(x)
                        visited.add(x)
            return farthest

        d1 = util(self, start)
        d2 = util(self, d1)
        return d1, d2

    def getTreeRoot(self):
        start, end = self.longestPahInTree()
        path = self.getPath(start, end)
        root = path[len(path) // 2]
        return root

    def getTree(self):
        self.root = self.getTreeRoot()

        self.parent = dict()
        self.parent[self.root] = None

        def DFS(self):
            stack = []
            visited = set()
            current = self.root
            self.depth[current] = 1
            visited.add(current)
            stack.append(current)
            while len(stack) > 0:
                v = stack.pop()
                for x in self.graph[v]:
                    if x not in visited:
                        stack.append(x)
                        visited.add(x)
                        self.parent[x] = v

                        self.depth[x] = self.depth[v] + 1

        DFS(self)
        time = 0

        def times(self, u, p):
            nonlocal time
            self.enter[u] = time
            time += 1
            for x in self.graph[u]:
                if x != p and x != u:
                    times(self, x, u)
            self.exit[u] = time
            time += 1

        times(self, self.root, None)

    def isAncestor(self, u, v):
        return self.enter[u] <= self.enter[v] and self.exit[v] <= self.exit[u]

    def getTreePath(self, u, v):
        p1 = []
        p2 = []
        lca = self.LCA(u, v)
        a = u
        b = v
        while a != lca:
            p1.append(a)
            if a == v:
                return p1
            a = self.parent[a]
        p1.append(a)
        while b != lca:

            p2.append(b)
            if b == u:
                return p2
            b = self.parent[b]

        return p1 + p2[::-1]

    def isLeaf(self, node):
        if len(self.graph[node]) == 1:
            return self.parent[node] == self.graph[node][0]
        return False

    def assignSubtreeWeights(self):

        def util(self, u):

            for x in self.graph[u]:

                if x != u and x != self.parent[u]:
                    self.subtree_weights[u] += util(self, x)
            self.sums[self.subtree_weights[u]].append(u)
            return self.subtree_weights[u]

        util(self, self.root)
        self.sorted_weighs = sorted(x for x in self.sums)

    def lcaUtil(self):
        n = len(self.graph)
        self.level = ceil(log2(n)) + 1
        for x in self.graph:
            self.parents[x] = [None for i in range(self.level)]
            self.parents[x][0] = self.parent[x]
        for i in range(1, self.level):
            for node in range(1, n + 1):
                if self.parents[node][i - 1] != None:
                    self.parents[node][i] = self.parents[self.parents[node][i - 1]][i - 1]

    def LCA(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        diff = self.depth[v] - self.depth[u]
        for i in range(self.level):
            if (diff >> i) & 1:
                v = self.parents[v][i]
        if u == v:
            return u
        for i in range(self.level - 1, -1, -1):
            if self.parents[u][i] != self.parents[v][i]:
                u = self.parents[u][i]
                v = self.parents[v][i]
        return self.parents[u][0]


def solve(g, total):
    ans = float('inf')

    for i in g.graph:
        si = g.subtree_weights[i]
        if si < total / 3:
            if (total - si) % 2 == 0:
                t = (total - si) // 2
                if t in g.sums:
                    arr = g.sums[t]
                    for x in arr:
                        if g.isAncestor(x, i):
                            continue
                        else:
                            ans = min(ans, t - si)
                            break
                else:
                    j = g.parent[i]
                    while j:
                        cs = g.subtree_weights[j] - si
                        if cs == t:
                            ans = min(ans, t - si)
                            break
                        j = g.parent[j]
        elif total / 3 <= si <= total / 2:
            t = si
            if si == total / 2 and total % 2 == 0:
                ans = min(ans, total // 2)
            if t in g.sums and len(g.sums[t]) > 1:
                arr = g.sums[t]
                for x in arr:
                    if not g.isAncestor(x, i):
                        ans = min(ans, 3 * si - total)
                        break
            else:
                cw = 3 * si - total
                j = i
                while j and g.parent[j]:
                    if g.subtree_weights[g.parent[j]] - g.subtree_weights[j] == si:
                        ans = min(ans, cw)
                        break
                    j = g.parent[j]

    if ans == float('inf'):
        return -1
    return ans


q = int(input().strip())
for _ in range(q):
    g = Graph()
    n = int(input().strip())
    weights = list(map(int, input().strip().split()))
    if n == 1:
        print(-1)
        continue

    for i in range(n - 1):
        u, v = map(int, input().strip().split())
        g.addEdge(u, v)
    g.getTree()
    total = sum(weights)
    for i in range(1, n + 1):
        g.subtree_weights[i] = weights[i - 1]
        g.weights[i] = weights[i - 1]
    g.assignSubtreeWeights()

    g.lcaUtil()
    print(solve(g, total))
