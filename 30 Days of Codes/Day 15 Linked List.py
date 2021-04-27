def insert(self, head, data):
    if not head:
        return Node(data)
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    return head
