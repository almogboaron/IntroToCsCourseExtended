# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = [313119265]

import random


############
# QUESTION 2
############

def text_2_16bits(text):
    "returns a string of bits represnting text"
    str = ""
    for c in text:
        binc = bin(ord(c))[2:]
        str += ((16 - len(binc)) * "0" + binc)
    return str


# Q2 - A, b
def bits_2_text(b_text):
    text = ""
    for i in range(0, len(b_text), 16):
        text += chr(int((b_text[i:i + 16]).lstrip("0"), 2))
    return text


# Q2 - B
def float_add(a, b):
    pass
############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):
    mat = []
    for i in range(0, len(lst), k):
        sublst = lst[i:i+k]
        selection_sort(sublst)
        mat.append(sublst)
    return mat


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    i = 0
    while len(lst)!=1:
        lst.append(merge(lst[i], lst[i+1]))
        i = i+2
        if i >= len(lst)-1:
            i = 0
    return lst









def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find(lst, s):
    for i in range(len(lst)):
        if s==lst[i]:
            return i
        return None


def sort_from_almost(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            temp = lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
    return None



def find_local_min(lst):
    for i in range(len(lst)):
        if (i==0 or lst[i]<=lst[i-1]) and( i==(len(lst)-1) or lst[i]<=lst[i+1] ):
            return i
    return None

############
# QUESTION 5
############

# a
def string_to_int(s):
    if s == "":  ##Sanety
        return None
    sum = 0
    chars = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}  # base 5
    for i in range(len(s)):
        sum += (5 ** (len(s) - 1 - i)) * chars[s[i]] ## Like Bits reading is from right to left ->
    return sum

def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    chars = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4} ## base 5
    scale = k-1
    res = ""
    while n!=0:
        key = n%(5**scale)
        res += chars[key]
        n = n-key*(5**(scale))
    return res

# c
def sort_strings1(lst, k):
    newlst = []
    helperlst=[-1 for i in range(5**k)]                 ## not mandatory but requaired in quastion  ##O(5^K)

    for str in lst :                                ##O(kn)
        if helperlst[string_to_int(str)] != -1:
            helperlst[string_to_int(str)+1] = str
        helperlst[string_to_int(str)] = str

    while len(helperlst) != 0:
        val = helperlst.pop(0)
        if val != -1 :
            newlst.append(val)
    return newlst

# e
def sort_strings2(lst, k):
    new_lst = string_to_int(lst[i])
    for i in range(len(5**k)):                      ##O(5^k)
        if i in new_lst:                            ##O(n)
            new_lst.append(int_to_string(k,i))      ##O(k)
    return new_lst

########
# Tester
########

def test():
    # q2 - a

    text = "Hi There"
    text_bits = text_2_16bits(text)
    if bits_2_text(text_bits) != text:
        print("error in text reconstruction")

    if text_bits.count("0") + text_bits.count("1") != len(text_bits):
        print("error: non binary characters in text_2_16bits")

    if len(text_bits) % 16 != 0:
        print("error wrong length for text_2_16bits output")

    # q2 - b
    a = "0100000000101000000000000000000000000000000000000000000000000000"
    b = "0011111111101000000000000000000000000000000000000000000000000000"
    res = "0100000000101001100000000000000000000000000000000000000000000000"
    if float_add(a, b) != res:
        print("error in float_add of 12 + 0.75")

    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]

    if find(almost_sorted_lst, 5) != 3:
        print("error in find")

    if find(almost_sorted_lst, 50) != None:
        print("error in find")

    sort_from_almost(almost_sorted_lst)
    if almost_sorted_lst != sorted(almost_sorted_lst):
        print("error in sort_from_almost")

    lst = [5, 6, 7, 5, 1, 1, 99, 100]
    pos = find_local_min(lst)
    if pos not in (0, 4, 5):
        print("error in find_local_min")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
test()