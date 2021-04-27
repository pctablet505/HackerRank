arr = []


def median():
    size = len(arr)
    if size == 0:
        print('Wrong!')
    elif size % 2 == 0:
        m = (arr[size // 2 - 1] + arr[size // 2]) / 2
        if int(m) == m:
            print(int(m))
        else:
            print(m)
    else:
        m = (arr[(size - 1) // 2])
        if int(m) == m:
            print(int(m))
        else:
            print(m)


def remove(l, r, x):
    if l > r:
        return False
    else:
        m = (l + r + 1) // 2
        if arr[m] == x:
            del arr[m]
            return True
        elif arr[m] < x:
            return remove(m + 1, r, x)
        else:
            return remove(l, m - 1, x)


def insert(l, r, x):
    if l == r:
        arr.insert(r, x)
    else:
        m = (l + r) // 2
        if arr[m] == x:
            arr.insert(m, x)
        elif arr[m] < x:
            insert(m + 1, r, x)
        else:
            insert(l, m, x)


for _ in range(int(input())):
    c, e = input().split()
    e = int(e)
    if c == 'a':
        if not arr:
            arr += [e]
        else:
            insert(0, len(arr), e)
        median()
    if c == 'r':
        if remove(0, len(arr) - 1, e):
            median()
        else:
            print('Wrong!')
