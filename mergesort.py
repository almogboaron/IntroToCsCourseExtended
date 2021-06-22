import time

from mergesort import * #make sure mergesort.py is at the same folder as this file
from quicksort import * #make sure quicksort.py is at the same folder as this file

print("3 way race")
for func in [quicksort, mergesort, sorted]:
    print(func.__name__)

    for n in [200, 400, 800]:
        print("n=", n, end=" ")
        rlst = randlist(n)

        t0 = time.perf_counter()
        for i in range(100):
            func(rlst) #sort is not inplace, so lst remains unchanged !
        t1 = time.perf_counter()
        print(t1-t0)
