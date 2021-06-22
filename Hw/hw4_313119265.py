# Skeleton file for HW4 - winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = [313119265]


############
# QUESTION 2
############

# c
def rec_slice_binary_search(lst, key):
    n = len(lst)
    if n <= 0:
        return None
    if key == lst[n // 2]:
        return n // 2
    elif key < lst[n // 2]:
        return rec_slice_binary_search(lst[0:n // 2], key)
    else:
        num = rec_slice_binary_search(lst[n // 2 + 1:n], key)
        if num != None:
            return num + n // 2 + 1


############
# QUESTION 3
############

# b
def had_local(n, i, j):
    assert 0 <= i, j < pow(2, n) and n >= 0
    if n == 0:
        return 0
    ###
    sign_i, sign_j = False, False
    half_of_rows = pow(2, n - 1)
    ###
    if i >= half_of_rows:
        i = i - half_of_rows
        sign_i = True
    if j >= half_of_rows:
        j = j - half_of_rows
        sign_j = True
    ### Negetive Mat ###
    if sign_i and sign_j:
        val_ij = had_local(n - 1, i, j)
        if val_ij == 0:
            return 1
        else:
            return 0
    ###
    return had_local(n - 1, i, j)


# d
had_complete = lambda n: [[had_local(n, i, j) for j in range(pow(2, n))] for i in range(pow(2, n))]


############
# QUESTION 4
############

# a
def find_zero_paths(m):
    dim_n = len(m)
    new_m = [[0 for i in range(dim_n)] for j in range(dim_n)]
    i, j = 0, 0
    while i <= dim_n - 1 and j <= dim_n - 1:
        ##Stoping Point and Check for 0
        if m[i][j] == 0:
            new_m[i][j] = 1
            if i == dim_n - 1 and j == dim_n - 1:
                return 1, new_m
        else:
            return 0, new_m
        ### check for Two Paths and Devietion into 2 matrixes
        if i < dim_n - 1 and j < dim_n - 1 and m[i][j + 1] == 0 and m[i + 1][j] == 0:
            m[i][j + 1] = 1
            first_path = find_zero_paths(m)
            m[i][j + 1] = 0
            m[i + 1][j] = 1
            second_path = find_zero_paths(m)
            m[i + 1][j] = 0
            r = first_path[0] + second_path[0]
            added_m = add_mat(first_path[1], second_path[1])
            return r, added_m
        ### I or J get to Max_Value going on one index
        elif i < dim_n - 1 and m[i + 1][j] == 0:
            i, j = i + 1, j
        elif j < dim_n - 1 and m[i][j + 1] == 0:
            i, j = i, j + 1
        ##
        else:
            return 0, []


def add_mat(a, b):
    n = []
    line = []
    for i in range(len(a)):
        for j in range(len(a)):
            line.append(a[i][j] + b[i][j])
        n.append(line)
        line = []
    return n


############
# QUESTION 5
############

# a
def find_max_profit(A, W, n, k):
    if n == -1:
        return 0
    ## Chosing if A[n] Will be in B
    val_An = A[n]
    val_Wn = W[n]
    if k - val_Wn < 0:
        return find_max_profit(A, W, n - 1, k)
    opt_1 = find_max_profit(A, W, n - 1, k - val_Wn) + val_An
    opt_2 = find_max_profit(A, W, n - 1, k)
    max_sum = max(opt_1, opt_2)
    return max_sum


# c
def find_max_profit_fast(A, W, n, k):
    max_dict = {}
    return find_max_mem(A, W, n, k, max_dict)


def find_max_mem(A, W, n, k, max_dict):
    if n == -1:
        return 0
    ## Chosing if A[n] Will be in B
    val_An = A[n]
    val_Wn = W[n]
    if k - val_Wn < 0:
        if ((n - 1), k) not in max_dict:
            max_dict[(n - 1), k] = find_max_mem(A, W, n - 1, k, max_dict)
            return max_dict[n - 1, k]
    if (n - 1, k) not in max_dict:
        max_dict[n - 1, k] = find_max_mem(A, W, n - 1, k, max_dict)
    if (n - 1, k - val_Wn) not in max_dict:
        max_dict[(n - 1, k - val_Wn)] = find_max_mem(A, W, n - 1, k - val_Wn, max_dict) + val_An
    return max(max_dict[n - 1, k], max_dict[(n - 1, k - val_Wn)])


############
# QUESTION 6
############

def distance(s1, s2):
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return distance(s1[1:], s2[1:])
    else:
        return 1 + min(distance(s1[1:], s2), distance(s1, s2[1:]), distance(s1[1:], s2[1:]))


def distance_fast(s1, s2):
    distance_dict = {}
    return distance_mem(s1, s2, distance_dict)


def distance_mem(s1, s2, distance_dict):
    if (s1, s2) not in distance_dict:
        if s1 == s2:
            return 0
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)
        if s1[0] == s2[0]:
            distance_dict[s1, s2] = distance_mem(s1[1:], s2[1:], distance_dict)
            return distance_dict[s1, s2]
        else:
            if (s1[1:], s2) not in distance_dict:
                distance_dict[s1[1:], s2] = distance_mem(s1[1:], s2, distance_dict)
            if (s1, s2[1:]) not in distance_dict:
                distance_dict[s1, s2[1:]] = distance_mem(s1, s2[1:], distance_dict)
            if (s1[1:], s2[1:]) not in distance_dict:
                distance_dict[s1[1:], s2[1:]] = distance_mem(s1[1:], s2[1:], distance_dict)
            distance_dict[s1,s2]= 1 + min(distance_dict[s1[1:], s2], distance_dict[s1, s2[1:]], distance_dict[s1[1:], s2[1:]])
            return distance_dict[s1,s2]
    return distance_dict[s1,s2]

########
# Tester
########

def test():
    # print matrix, use this function only to check your results.
    def print_matrix(A):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in A]))

    # Q2-c
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    key = 8
    if (rec_slice_binary_search(lst, key) != 7):
        print("Error in rec_slice_binary_search")

    # Q3-b
    if (had_local(2, 2, 2) != 1):
        print("Error in had_local")

    # Q4-a
    m = [[0, 0, 0, 2, 4, 6],
         [0, 4, 0, 2, 3, 4],
         [0, 0, 0, 3, 2, 4],
         [2, 4, 0, 0, 0, 0],
         [3, 6, 0, 4, 6, 0],
         [3, 0, 0, 0, 0, 0]]
    rr, rm = find_zero_paths(m)
    if (rr != 4):
        print("Error in find_zero_path")
    print_matrix(rm)

    # Q5-a
    A = [20, 5, 10, 40, 15, 25]
    W = [1, 2, 3, 8, 7, 4]
    k = 10
    if (find_max_profit(A, W, len(A) - 1, k) != 60):
        print("Error in find_max_profit")
    # Q5-c
    if (find_max_profit_fast(A, W, len(A) - 1, k) != 60):
        print("Error in find_max_profit_fast")

    # Q6
    if distance('computer', 'commuter') != 1 or \
            distance('sport', 'sort') != 1 or \
            distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
        print("Error in distance")

    if distance_fast('computer', 'commuter') != 1 or \
            distance_fast('sport', 'sort') != 1 or \
            distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
        print("Error in distance_fast")


test()
