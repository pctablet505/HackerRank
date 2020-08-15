def has_cycle(head):
    a = set()
    temp = head
    while temp:
        if temp in a:
            return True
        a.add(temp)
        temp = temp.next
    return False
