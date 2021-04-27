cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]

    # return a list of fibonacci numbers
