def parse_primes(filename):
    primes = []
    with open(filename, "r") as f:
        for line in f:
            primes += [int(num_str) for num_str in line.split(" ")[:-1] if num_str]
    return set(primes)


def check_goldbach_for_num(n, primes_set):
    for a in primes_set:
        if n - a in primes_set:
            return True
    return False


def check_goldbach_for_range(limit, primes_set):
    for i in range(4, limit, 2):
        if not check_goldbach_for_num(i, primes_set):
            return False
    return True


# 5c1
def check_goldbach_for_num_stats(n, primes_set):
    x = sum([1 for a in primes_set if (n - a in primes_set)]) // 2
    if n / 2 in primes_set:
        return x+1
    return x

# 5c2
def check_goldbach_stats(limit, primes_set):
    d = {}
    for n in range(4, limit, 2):
        id = check_goldbach_for_num_stats(n, primes_set)
        if id in d.keys():
            d[id] += 1
            continue
        d[id] = 1
        print(d)
    return d
############import time


primes_set = parse_primes('primes.txt')

if check_goldbach_stats(11, primes_set) != {1: 3, 2: 1}:
    print("error in check_goldbach_stats")
