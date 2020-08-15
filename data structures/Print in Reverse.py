def reversePrint(head):
    a = []
    h = head
    while h:
        a.append(h.data)
        h = h.next
    for x in range(len(a) - 1, -1, -1):
        print(a[x])
