def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def selection_sort(lst):
    ''' sort lst (in-place) '''
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i+1,n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None



"""
import time
import random

print("Measuring time sor selection_sort")

for n in [1000,2000,4000]:
    lst = list(range(n))
    random.shuffle(lst)
    t0 = time.perf_counter()   # go!
    selection_sort(lst)
    t1 = time.perf_counter()   # stop.
    print("n=", n, t1-t0)

"""
