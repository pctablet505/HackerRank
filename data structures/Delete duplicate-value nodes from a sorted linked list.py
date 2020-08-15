def removeDuplicates(head):
    node=head
    while node:
        if node.next !=None:
            if node.data==node.next.data:
                temp=node.next
                node.next=temp.next
            else:
                node=node.next
        else:
            return head