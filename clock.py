import time        # imports the Python time module

def elapsed(expression, number=1):
    ''' computes elapsed time for executing code number
        times (default is 1 time). expression should be
        a string representing a Python expression.'''
    t1 = time.perf_counter()
    for i in range(number):
        eval(expression)
    t2 = time.perf_counter()
    return t2-t1
