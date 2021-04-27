def wrapper(f):
    def fun(l):
        numbers = []
        for x in l:
            numbers.append(x[-10:])
        numbers.sort()
        for number in numbers:
            print('+91 {} {}'.format(number[:5], number[-5:]))

    return fun
