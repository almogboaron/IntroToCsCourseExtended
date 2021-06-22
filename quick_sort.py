import random  # package for generating (pseudo) random elements


def quicksort(lst):
    """ quick sort of lst """
    if len(lst) <= 1:
        return lst
    else:
        # pivot = random.choice(lst) # select a random element from list
        pivot = lst[0]  # for a deterministic quicksort

        smaller = [elem for elem in lst if elem < pivot]
        equal = [elem for elem in lst if elem == pivot]
        greater = [elem for elem in lst if elem > pivot]

        return quicksort(smaller) + equal + quicksort(greater)
        # two recursive calls


def ordlist(n):
    """ generates an ordered list [0,1,...,(n-2),(n-1)] """
    return [i for i in range(0, n)]


def randlist(n):
    """ generates a list of n random elements from [0,...,n**2] """
    return [random.randint(0, n ** 2) for i in range(0, n)]


"""
import time

for n in [200, 400, 800]:
    print("n=", n, end=" ")
    #lst = ordlist(n)
    lst = randlist(n)
    t0 = time.perf_counter()
    for i in range(100):
        quicksort(lst) #sort is not inplace, so lst remains unchanged !
    t1 = time.perf_counter()
    print(t1-t0)

"""


