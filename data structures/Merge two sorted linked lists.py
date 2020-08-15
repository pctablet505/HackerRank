def mergeLists(head1, head2):
    p, q = head1, head2
    newlist = SinglyLinkedList()
    while p and q:
        if p.data <= q.data:
            newlist.insert_node(p.data)
            p = p.next
        else:
            newlist.insert_node(q.data)
            q = q.next
    if p == None and q:
        while q:
            newlist.insert_node(q.data)
            q = q.next
    if q == None and p:
        while p:
            newlist.insert_node(p.data)
            p = p.next
    return newlist.head
