def slow_gcd(k, m):
    """ greatest common divisor of two integers - naive inefficient method """
    assert isinstance(k, int) and isinstance(m, int)  # type checking: k and m both integers

    k, m = abs(k), abs(m)  # Simultaneous assignment, gcd invariant to abs.
    # Both k,m now non-negative
    if k < m:
        k, m = m, k  # Now m <= k

    for g in range(m, 0, -1):  # from m downward to 1
        if k % g == m % g == 0:  # g divides both k and m?
            return g

    return None  # should never get here, 1 divides all


def gcd(k, m):
    """ greatest common divisor of two integers - Euclid's algorithm """
    assert isinstance(k, int) and isinstance(m, int)  # type checking: k and m both integers

    k, m = abs(k), abs(m)  # Simultaneous assignment, gcd invariant to abs.
    # Both k,m now non-negative
    if k < m:
        k, m = m, k  # Now m <= k

    # print(k,m)
    while m > 0:
        k, m = m, k % m
        # print(k,m)

    return k

