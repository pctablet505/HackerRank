

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    newlist=SinglyLinkedList()
    temp=head
    while temp:
        new_node=SinglyLinkedListNode(temp.data)
        new_node.next=newlist.head
        newlist.head=new_node
        temp=temp.next
    return newlist.head

