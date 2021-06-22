from select_sort import selection_sort  # file select_sort.py must be in the same folder


def merge_by_sort(A, B):  # Not efficient, does not exploit the fact that each of A and B are sorted
    """ merging two lists into a sorted list """
    C = A + B
    selection_sort(C)
    return C


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0;
    b = 0;
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    if a == n:  # A was completed
        while b < m:
            C[c] = B[b]
            b += 1
            c += 1
    else:  # B was completed
        while a < n:
            C[c] = A[a]
            a += 1
            c += 1

    return C


"""
import time
import random  

for merge_func in [merge_by_sort, merge]:
    print(merge_func.__name__)

    for n in [1000,2000,4000]:
        lst1 = [random.choice(range(10000)) for i in range(n)]
        lst1.sort()
        lst2 = [random.choice(range(10000)) for i in range(n)]
        lst2.sort()

        t0 = time.perf_counter()   # go!
        merge_func(lst1,lst2)
        t1 = time.perf_counter()   # stop.

        print("n=", n, t1-t0)
"""


