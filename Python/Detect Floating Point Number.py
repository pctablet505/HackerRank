test = int(input())
for x in range(test):
    result = True
    point = False
    s = input()
    result = False
    if s.count('.') == 1:
        left, right = s.split(sep='.')
        if right.isdigit():
            if (left[0] in '+-' and (left[1:].isdigit() or left[1:] == '')) or left.isdigit():
                result = True

    print(result)
