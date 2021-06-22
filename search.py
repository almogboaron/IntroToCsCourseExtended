def sequential_search(lst, key):
    """ Iterate lst sequentially to search for key
        lst need not be sorted for sequential search to work.
        returns index of match or None if not found """
    for i in range(len(lst)):
        if lst[i] == key:
            return i

    #We get here when the key is not in the list
    #print(key, "not found")
    return None



def sequential_search_back(lst, key):
    lst = lst[::-1] # reversed lst
    for i in range(len(lst)):
        if lst[i] == key :
            return len(lst)-i-1

    #We get here when the key is not in the list
    #print(key, "not found")
    return None




def binary_search(lst, key):
    """ lst better be sorted for binary search to work """
    n = len(lst)
    left = 0
    right = n-1

    while left <= right:
        mid = (left+right)//2    # middle rounded down
        if key == lst[mid]:      # item found
            return mid
        elif key < lst[mid]:     # item cannot be in top half
            right = mid-1
        else:                    # item cannot be in bottom half
            left = mid+1

    #print(key, "not found")
    return None



####################################################
## Time measurements of sequential vs. binary search
####################################################


import time

REPEAT = 20 #repeat execution several times, for more significant statistics

for f in [sequential_search, binary_search]:
    print(f.__name__)

    for n in [10**6, 2*10**6, 4*10**6]:
        print("n=", n)

        L = [i for i in range(n)] #generates the ordered list 0,1,2,...,n-1
        key = -1 #key that DOES NOT exist in the list (worst case)

        t0 = time.perf_counter()
        for i in range(REPEAT):
            res = f(L, key) # key not found
        t1 = time.perf_counter()
        print("time for", REPEAT, "executions:", (t1-t0))


