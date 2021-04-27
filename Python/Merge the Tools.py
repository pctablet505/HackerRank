def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    st = []
    x = 0
    while x < n:
        s = ''
        for j in range(k):
            s += string[x + j]
        st.append(s)
        x += k
    new = []
    for strings in st:
        s = ''
        for x in strings:
            if x not in s:
                s += x
        new.append(s)

    for values in new:
        print(values)
