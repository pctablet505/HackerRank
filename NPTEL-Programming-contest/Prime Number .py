p = set()
p.add(2)


def primality(n):
    global p
    if n in p:
        return True
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        p.add(n)
        return True


n = int(input().strip())
if primality(n):
    print('yes')
else:
    print('no')
