""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
s = ''


def inOrder(root):
    global s
    if root:
        inOrder(root.left)
        s += str(root.data) + ' '
        inOrder(root.right)


def check_binary_search_tree_(root):
    inOrder(root)
    original = list(map(int, s.split()))
    new = list(dict.fromkeys(sorted(original)))
    return all(original[i] == new[i] for i in range(len(original)))
