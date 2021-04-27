

    def getHeight(self,root):
        if not root:
            return -1
        return 1+max(self.getHeight(root.left),self.getHeight(root.right))
        #Write your code here

