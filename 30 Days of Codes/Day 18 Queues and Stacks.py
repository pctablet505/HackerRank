
from queue import deque
class Solution:
    stack=[]
    queue=deque()
    def pushCharacter(self,ch):
        self.stack.append(ch)
    def enqueueCharacter(self,ch):
        self.queue.appendleft(ch)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.pop()

    # Write your code here

