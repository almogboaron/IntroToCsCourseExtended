def linear_combination(x, y):
    y = 2 * y
    return x + y


def modify_list(lst, i, val):
    """ assign val to lst[i] does not return any value """
    if len(lst) > i:
        lst[i] = val
    return None


def increment(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] + 1
    # no value returned (same as return None)


def nullify(lst):
    print(hex(id(lst)))
    lst = []
    print(hex(id(lst)))
    # no value returned (same as return None)


s = 0


def summation_local(n):
    s = sum(range(1, n + 1))
    # no value returned (same as return None)


def summation_global(n):
    global s
    s = sum(range(1, n + 1))
    # no value returned (same as return None)


def mydivmod(a, b):
    """ integer quotient and remainder of a divided by b """
    return a // b, a % b
