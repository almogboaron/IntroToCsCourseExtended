def naturals():
    """ a generator for all natural numbers """
    # print("start naturals")
    n = 0
    while True:
        yield n
        n += 1


# nat = naturals()
# for i in range(10):
#    print(next(nat))

# for i in range(10):
#    print(next(naturals()))


def fib():
    """ a generator for all Fibonacci numbers """
    a, b = 1, 1
    yield a
    while True:
        yield b
        a, b = b, a + b


# fib_gen = fib()
# for i in range(10):
#    print(next(fib_gen))

def get_fib(n):
    ''' return the n'th fibonacci number '''
    g = fib()
    for i in range(n - 1):
        next(g)  # no need to store it
    return next(g)


# fib_gen = fib()
# print(get_fib(10))


def merge(gen1, gen2):
    """ on input gen1, gen2, two generators of infinite sorted streams,
        produces the sorted merge of the two """

    left = next(gen1)
    right = next(gen2)
    while True:
        if left <= right:
            yield left
            left = next(gen1)
        else:
            yield right
            right = next(gen2)

        # nat = naturals()


# fib_gen = fib()
# merged = merge(nat, fib_gen)
# for i in range(10):
#    print(next(merged))


def f(n):
    """ a finite generator """
    for i in range(n):
        yield i


# g1 = f(2**100)
# same as:
# g2 = (x for x in range(2**100)) # note the () instead of []


def permutations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in permutations(seq[1:]):  # all except 1st
            for i in range(len(seq)):  # location to insert 1st
                yield perm[:i] + seq[0:1] + perm[i:]


