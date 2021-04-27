

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    if llist is None:
        llist=SinglyLinkedListNode(data)
        return llist

    new_node=SinglyLinkedListNode(data)
    new_node.next=llist
    llist=new_node
    return llist

