import random

def is_prime(m, show_witness=False):

    """ probabilistic test for m's compositeness """''

    for i in range(0, 100):
        a = random.randint(1, m - 1) # a is a random integer in [1...m-1]
        if modpower(a, m - 1, m) != 1:
            if show_witness:  # caller wishes to see a witness
                print(m, "is composite", "\n", a, "is a witness, i=", i + 1)
            return False

    return True

def modpower(a, b, c):
    """ computes a**b modulo c, using iterated squaring """
    result = 1
    while b > 0: # while b is nonzero
        if b % 2 == 1: # b is odd
            result = (result * a) % c
        a = (a*a) % c
        b = b // 2
    return result

def prob_prime(n, sample):
    cnt = 0
    for i in range(sample):
        m = random.randint(2**(n-1), 2**n - 1)
        cnt += is_prime(m)
    return cnt / sample

print(prob_prime(3,10**4))