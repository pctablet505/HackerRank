def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    substrings = []
    x = 0
    while x < n:
        s = ''
        for j in range(k):
            if string[x + j] not in s:
                s += string[x + j]
        substrings.append(s)
        x += k

    for values in substrings:
        print(values)
