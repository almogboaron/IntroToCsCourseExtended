def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n+m)]

    a=0; b=0; c=0
    while  a<n  and  b<m: #more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    C[c:] = A[a:] + B[b:] #append remaining elements (one of those is empty)

    return C



def mergesort(lst):
    """ recursive mergesort """
    n = len(lst)
    if n<=1:
        return lst
    else:            #two recursive calls
        return merge(mergesort(lst[0:n//2]),  \
                     mergesort(lst[n//2:n]))


