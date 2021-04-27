# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = SinglyLinkedListNode(data)
    return head
