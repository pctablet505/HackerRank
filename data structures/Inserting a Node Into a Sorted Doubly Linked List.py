# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if node.data <= head.data:
        node.next = head
        head.prev = node
        head = node
        return head
    temp = head
    while temp != None:
        if temp.next == None or temp.next.data >= node.data:
            node.prev = temp
            if temp.next != None:
                temp.next.prev = node
                node.next = temp.next
            temp.next = node
            return head
        temp = temp.next

    # while temp
