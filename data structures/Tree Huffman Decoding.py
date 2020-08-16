"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    string = ''
    t = root
    for i in range(len(s)):
        if s[i] == '0':
            t = t.left
        else:
            t = t.right
        if t.left == t.right == None:
            string += t.data
            t = root
    print(string)
