def deleteNode(head, position):
    if position == 0:
        head = head.next
        return head
    node = head

    for i in range(position - 1):
        node = node.next
    node.next = node.next.next
    return head
