# Skeleton file for HW2 - Winter 2021 - extended intro to CS

# Add your implementation to this file

# you may NOT change the signature of the existing functions.

# Change the name of the file to include your ID number (hw2_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["313119265"]

import random  # loads python's random module in order to use random.random() in question 2


############
# QUESTION 1
############

def poker_hand(hand):
    # ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
    cards = str.split(hand)
    straight_check = 0
    flush_check = 0
    for letter in "HDCS":
        counter = 0
        for card in cards:
            if letter in card:
                counter += 1
        if counter == 5:
            flush_check = 1
            break
        if counter in range(1, 5):
            break
    seg = "23456789TJQKA"
    myhand = []
    straight_counter = 0
    straight_check = 0
    for letter in seg:
        counter = 0
        for card in cards:
            if letter in card:
                counter += 1
        if counter == 0:
            straight_counter = 0
        elif counter == 1:
            straight_counter += 1
            if straight_counter == 5:
                straight_check = 1
        elif counter == 2:
            myhand.append(2)
        elif counter == 3:
            if sum(myhand) == 2:
                return
            myhand.append(3)
        elif counter == 4:
            return "Four of a Kind"
    if flush_check:
        if straight_counter == 5:
            return "Royal Flush"
        if straight_check:
            return "Straight Flush"
        return "Flush"
    if straight_check:
        return "Straight"
    if sum(myhand) == 2:
        return "One Pair"
    if sum(myhand) == 3:
        return "Three of a Kind"
    if sum(myhand) == 4:
        return "Two Pairs"
    if sum(myhand) == 5:
        return "Full House"
    return "High Card"


############
# QUESTION 2
############

# 2a
def coin():
    return random.random() > 0.5


# 2b
def uniform(a, b):
    assert a < b
    return a + (b - a) * random.random()


# 2c
def choice(seq):
    return seq[int(random.random() * len(seq))]


# 2d
def weighted_choice(seq, weights):
    assert sum(weights) == 1 and len(seq) == len(weights)
    rand = random.random()
    sumnum = 0
    for i, weight in enumerate(weights):
        sumnum += weight
        if rand < sumnum:
            return seq[i]


# 2e
def get_biased_coin(p):
    return lambda: random.random() < p


def test_biased_coin(p, num_flips):
    sumtrue = 0
    func = get_biased_coin(p)
    for i in range(num_flips):
        if func():
            sumtrue += 1
    return sumtrue / num_flips


############
# QUESTION 3
############

# 3a
def has_repeat1(s, k):
    ezer = []
    for i in range(len(s) - k + 1):
        if s[i:i + k] in ezer:
            return True
        else:
            ezer.append(s[i:i + k])
    return False

    # 3b


def has_repeat2(s, k):
    for i in range(len(s) - k + 1):
        seq = s[i:i + k]
        for j in range(1, len(s[i:]) - k + 1):
            seq_j = s[i + j:i + j + k]
            if seq == seq_j:
                return True
    return False


############
# QUESTION 4
############

def interpolate(xy, x_hat):
    result = []
    for i in x_hat:
        for j in range(len(xy)):
            if i == xy[j][0]:
                result.append(xy[j])
                break
            if xy[j][0] < i < xy[j + 1][0]:
                middle = (xy[j][0] + xy[j + 1][0]) / i
                result.append((i, (xy[j][1] + xy[j + 1][1]) / middle))
                break
    return result


############
# QUESTION 5
############
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
        return x + 1
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
    return d


############
# QUESTION 6
############

# 6a
def add(bin1, bin2):
    maxzeros = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(maxzeros)
    bin2 = bin2.zfill(maxzeros)
    result = ""
    carry = False
    for b1, b2 in zip(bin1[::-1], bin2[::-1]):
        if b1 == b2:
            if b1 == "1":
                if carry:
                    result = "1" + result
                else:
                    result = "0" + result
                    carry = True
            elif b1 == "0":
                if carry:
                    result = "1" + result
                    carry = False
                else:
                    result = "0" + result
        else:
            if carry:
                result = "0" + result
            else:
                result = "1" + result
    if carry:
        result = "1"+ result
    return result


# 6b
# Checked Online Algoritem
def sub(bin1, bin2):
    if bin2 == "0":
        return bin1
    if bin1 == bin2:
        return "0"
    mash_1 = ""
    for i in bin2.zfill(len(bin1)):
        if i == "0":
            mash_1 = mash_1+"1"
        else:
            mash_1 = mash_1+"0"
    mash_2 = add(mash_1, "1")
    result = add(mash_2, bin1)
    if len(result) > len(bin1):
        result = result[1:]
    result = result.lstrip("0")

    return result


# 6c
def inc(binary):
    return add(binary,"1")


# 6d
def dec(binary):
    return sub(binary,"1")


# 6e
def mult(bin1, bin2):
    if bin1=="0" or bin2=="0":
        return "0"
    sum = "0"
    for i , bit in enumerate(bin2[::-1]):
        if bit == "0":
            continue
        else:
            sum = add(bin1+i*"0", sum)
    return sum




########
# Tester
########

def test():
    # 1
    if poker_hand("5H 5C 6S 7S KD") != 'One Pair' or \
            poker_hand("5D 8C 9S JS AC") != 'High Card' or \
            poker_hand("3D 6D 7D TD QD") != 'Flush' or \
            poker_hand("3C 3D 3S 9S 9D") != 'Full House' or \
            poker_hand("AC TC JC KC QC") != 'Royal Flush' or \
            poker_hand("AC TC JC KC QD") != 'Straight':
        print("error in poker_hand")

    # 2a
    if coin() not in [True, False]:
        print("error in coin")

    # 2b
    if not (-0.2 <= uniform(-0.2, 1.3) < 1.3):
        print("error in uniform")

    # 2c
    if choice(range(7)) not in range(7):
        print("error in choice")

    # 2d
    if weighted_choice([1, 2, 3], [0.1, 0.1, 0.8]) not in [1, 2, 3]:
        print("error in weighted_choice")

    # 2e
    if not callable(get_biased_coin(0.8)) or get_biased_coin(0.3)() not in [True, False]:
        print("error in get_biased_coin")

    # 2f
    if abs(test_biased_coin(0.3, 100000) - 0.3) > 0.01:
        print("error in test_biased_coin")

    # 3a
    if not has_repeat1("ababa", 3) or \
            has_repeat1("ababa", 4) or \
            not has_repeat1("aba", 1):
        print("error in has_repeat1()")

    # 3b
    if not has_repeat2("ababa", 3) or \
            has_repeat2("ababa", 4) or \
            not has_repeat2("aba", 1):
        print("error in has_repeat2()")

    # 4
    if interpolate([(1, 10), (4, 40)], [4, 2, 3]) != [(4, 40), (2, 20.0), (3, 30.0)] or \
            interpolate([(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)], [-2.5, -1.5, 0.5, 1.5, 2.5]) != [
        (-2.5, 6.5), (-1.5, 2.5), (0.5, 0.5), (1.5, 2.5), (2.5, 6.5)]:
        print("error in interpolate")

    # 5a
    if not check_goldbach_for_num(10, {2, 3, 5, 7}) or \
            check_goldbach_for_num(10, {2, 3}):
        print("error in check_goldbach_for_num()")

    # 5b
    if not check_goldbach_for_range(20, {2, 3, 5, 7, 11}) or \
            check_goldbach_for_range(21, {2, 3, 5, 7, 11}):
        print("error in check_goldbach_for_range()")

    # 5c
    primes_set = parse_primes('primes.txt')
    if check_goldbach_for_num_stats(20, primes_set) != 2 or \
            check_goldbach_for_num_stats(10, primes_set) != 2:
        print("error in check_goldbach_for_num_stats()")

    if check_goldbach_stats(11, primes_set) != {1: 3, 2: 1}:
        print("error in check_goldbach_stats")

    # 6a
    if add("10", "0") != "10" or \
            add("0", "0") != "0" or \
            add("1001", "11") != "1100":
        print("error in add")

    # 6b
    if sub("10", "0") != "10" or \
            sub("0", "0") != "0" or \
            sub("1000", "11") != "101":
        print("error in sub")

    # 6c
    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("error in inc")

    # 6d
    if dec("1") != "0" or \
            dec("101") != "100" or \
            dec("100") != "11" or \
            dec(dec("100")) != "10":
        print("error in dec")

    # 6e
    if mult("0", "10") != "0" or \
            mult("0", "0") != "0" or \
            mult("10", "1010") != "10100" or \
            mult("1", "1011") != "1011" or \
            mult("11", "111") != "10101":
        print("error in mult")

import time

primes_set = parse_primes('primes.txt')
t0=time.perf_counter()
check_goldbach_for_range(1000, primes_set)
t1=time.perf_counter()
print("Range Runing Time :", t1-t0)
t0=time.perf_counter()
check_goldbach_stats(1000, primes_set)
t1=time.perf_counter()
print("Stats Runing Time :", t1-t0)