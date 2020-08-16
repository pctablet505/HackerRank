def reverse(head):
    rlist = DoublyLinkedList()
    temp = head
    while temp.next != None:
        temp = temp.next
    while temp:
        rlist.insert_node(temp.data)
        temp = temp.prev
    return rlist.head
