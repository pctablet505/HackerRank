

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    result=True
    l1=llist1
    l2=llist2
    while l1 or l2:
        if (l1 and(not l2)) or(l2 and(not l1)):
            result=False
            break
        if l1.data!=l2.data:
            result=False
        l1=l1.next
        l2=l2.next
    return result

