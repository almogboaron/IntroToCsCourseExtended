def root(f,l,u,eps = 10**-4,tol = 100):
    for i in range(tol):
        m = (l+u)/2
        fm = f(m)
        if abs(fm)<eps:
            print("found an approximated root")
            return m
        elif not l<m<u:
            print("search interval to small")
            return None
        elif fm<0:
            l=m
        else:
            u=m

f = lambda x:x**2-x-1
print(root(f,0,3))
