def print_rangoli(size):
    for j in range(1, size + 1):
        s = [];
        a = 97 + size - 1
        for i in range(j - 1):
            s.append(chr(a))
            a -= 1
        s.append(chr(a))
        a += 1
        for i in range(j - 1):
            s.append(chr(a))
            a += 1
        b = '-'.join(s)
        print('{}'.format(b).center((size * 4 - 3), '-'))
    for j in range(size - 1, 0, -1):
        s = [];
        a = 97 + size - 1
        for i in range(j - 1):
            s.append(chr(a))
            a -= 1
        s.append(chr(a))
        a += 1
        for i in range(j - 1):
            s.append(chr(a))
            a += 1
        b = '-'.join(s)
        print('{}'.format(b).center((size * 4 - 3), '-'))

    # your code goes here
