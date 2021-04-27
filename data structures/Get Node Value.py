# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    counter = head
    length = 0
    while counter is not None:
        length += 1
        counter = counter.next
    position = length - 1 - positionFromTail
    if position < 0:
        return False
    temp = head
    for _ in range(position):
        temp = temp.next
    return temp.data
