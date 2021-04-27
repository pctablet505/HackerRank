str1 = [x for x in input()]
str1.sort()
lower, upper, odd, even = [], [], [], []
for x in str1:
    if x.islower():
        lower.append(x)
    elif x.isupper():
        upper.append(x)
    elif x.isdigit():
        if int(x) % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
print(''.join(lower + upper + odd + even))
