

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    rlist=DoublyLinkedList()
    temp=head
    while temp.next!=None:
        temp=temp.next
    while temp:
        rlist.insert_node(temp.data)
        temp=temp.prev
    return rlist.head


