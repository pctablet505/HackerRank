


# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node=SinglyLinkedListNode(data)
    if position==0:        
        new_node.next=head
        head=new_node
        return head
    temp=head
    for i in range(position-1):
        temp=temp.next
    new_node.next=temp.next
    temp.next=new_node
    return head

