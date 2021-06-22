import time


def elapsed(expression, number=1):
    ''' computes elapsed time for executing code
    number of times (default is 1 time). expression should
    be a string representing a Python expression. '''
    t1 = time.perf_counter()
    for i in range(number):
        eval(expression)
    t2 = time.perf_counter()
    return t2 - t1


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def count_fibonacci(n):
    """ recursive Fibonacci + counting no. of function invocations """
    global count
    count += 1
    if n < 2:
        return 1
    return count_fibonacci(n - 1) + count_fibonacci(n - 2)


def fibonacci2(n):
    """ Envelope function for fib2,
        employing memoization in a dictionary """

    fib_dict = {0: 1, 1: 1}  # initial dictionary with first two elements
    return fib2(n, fib_dict)


def fib2(n, fib_dict):
    # print(n)  # diagnostic printing
    if n not in fib_dict:
        res = fib2(n - 1, fib_dict) + fib2(n - 2, fib_dict)
        fib_dict[n] = res
    return fib_dict[n]


def fib2_reverse(n, fib_dict):
    # print(n)  # diagnostic printing
    if n not in fib_dict:
        res = fib2_reverse(n - 2, fib_dict) + fib2_reverse(n - 1, fib_dict)
        fib_dict[n] = res
    return fib_dict[n]


def fibonacci3(n):
    """ iterative Fibonacci, employing
        keeps all values in a list """
    if n < 2:
        return 1
    else:
        fibb = [0 for i in range(n + 1)]
        fibb[0] = fibb[1] = 1  # initialize
        for k in range(2, n + 1):
            fibb[k] = fibb[k - 1] + fibb[k - 2]  # update next element
        return fibb[n]


def fibonacci4(n):
    """ fibonacci in O(1) memory """
    if n < 2:
        return 1  # base case
    else:
        prev = 1
        curr = 1
        for i in range(n - 1):  # n-1 iterations (count carefully)
            curr, prev = prev + curr, curr
        # simultaneous assignment
        return curr


def closed_fib(n):
    """ code for closed form Fibonacci number """
    return round(((1 + 5 ** 0.5) ** (n + 1) - (1 - 5 ** 0.5) ** (n + 1)) / (2 ** (n + 1) * 5 ** 0.5))
