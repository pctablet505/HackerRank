

def print_from_stream(n, stream=None):
    if stream==None:
        stream=EvenStream()
    else:
        stream=OddStream()
    for _ in range(n):
        print(stream.get_next())

