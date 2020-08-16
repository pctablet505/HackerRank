from collections import OrderedDict
bill=OrderedDict()
no_of_items=int(input())
for _ in range(no_of_items):
    item,space,no=input().rpartition(' ')
    bill[item]=bill.get(item,0)+int(no)
for items in bill:
    print(items,bill.get(items))
