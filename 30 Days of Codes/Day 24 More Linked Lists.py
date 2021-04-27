

    def removeDuplicates(self,head):
        curr=head
        while curr.next:
            if curr.next.data==curr.data:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head


