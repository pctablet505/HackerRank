def wrap(string, max_width):
    s = ''
    i = 0
    for letter in string:
        s += letter
        i += 1
        if i % max_width == 0:
            s += '\n'
    return s
