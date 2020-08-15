def findMergeNode(head1, head2):
    t1,t2=head1,head2
    from queue import Queue
    q=set()
    while t1:
        q.add(t1)
        t1=t1.next
    while t2:
        if t2 in q:
            return t2.data
        else:
            t2=t2.next
