

    def levelOrder(self,root):
        from collections import deque
        res=[]
        q=deque()
        q.append(root)
        while q:
            c=q.popleft()
            res.append(c.data)
            if c.left:
                q.append(c.left)
            if c.right:
                q.append(c.right)
        for x in res:
            print(x,end=' ')


