import bisect
import decimal


def median():
    global lst
    if not lst:
        print("Wrong!")
        return
    leng = len(lst)
    mid = leng // 2
    if leng % 2 != 0:
        print((lst[mid]))
    else:
        x = lst[mid]
        y = lst[mid - 1]
        print(('%f' % decimal.Decimal(((int(x) + int(y)) / 2))).rstrip('0').rstrip('.'))


lst = []
N = int(input())
for _ in range(N):
    q, e = input().strip().split(' ')
    e = int(e)
    if q == 'r':
        x = bisect.bisect_left(lst, e)
        if x < len(lst) and lst[x] == e:
            lst.pop(x)
        else:
            print("Wrong!")
            continue
    else:
        bisect.insort_left(lst, int(e))
    median()
