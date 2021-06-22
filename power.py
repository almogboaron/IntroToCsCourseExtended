def naive_power(a, b):
    ''' Computes a**b using all successive powers a, a**2, a**3,...
        Assume a,b are integers and b>=0  '''

    result = 1  # a**0

    for i in range(0, b):  # b iterations
        result *= a

    return result


def power1(a, b):
    ''' Computes a**b using iterated squaring
        Assume a,b are integers and b>=0  '''

    result = 1  # a**0

    while b > 0:  # b has more digits
        if b % 2 == 1:  # b is odd
            result *= a
            b = b - 1
        else:
            a = a * a
            b = b // 2

    return result


def power2(a, b):
    ''' Computes a**b using iterated squaring
        Assume a,b are integers and b>=0  '''

    result = 1  # a**0

    while b > 0:  # b has more digits
        if b % 2 == 1:  # b is odd
            result *= a
        a = a * a
        b = b // 2  # discard b's rightmost bit

    return result


def modpower(a, b, c):
    ''' Computes a**b mod c using iterated squaring
        Assume a,b,c are integers, b>=0, c>=2  '''

    result = 1  # a**0

    while b > 0:
        if b % 2 == 1:  # b is odd
            result = (result * a) % c  # note the %
        a = (a * a) % c  # note the %
        b = b // 2

    return result

