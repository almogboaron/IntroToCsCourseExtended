import math

def diff(f, h=0.001):
    """ Returns the derivative of a
        one parameter real valued function f.
        When h is not specified, default value h=0.001 is used
    """
    return (lambda x: (f(x+h)-f(x))/h)


def integral(f, h=0.001):
     """ definite integral of f between a, b """
     return lambda a,b:    \
                h * sum(f(a+i*h) \
			for i in range(0, int((b-a)/h )))



##########################################
## Some real valued functions to play with
##########################################

def square(x):
     return x**2

def penta(x):
     return x**5

def sin_by_million(x):
    return math.sin(10**6*x)
