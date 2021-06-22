# complexity is O(|R|^2 * n^3) worst case,
#  where n=|st| and |R| is the number of rules = number of values stored
#  in the sets in rule_dict

def CYK(st, rule_dict, start_var):
    ''' can string st be generated from grammar? '''
    n = len(st)

    # table for the dynamic programming algorithm
    table = [[None for j in range(n + 1)] for i in range(n)]
    # Initialize the relevant triangular region with empty sets
    for i in range(n):
        for j in range(i + 1, n + 1):
            table[i][j] = set()

    # Fill the table cells representing substrings of length 1
    fill_length_1_cells(table, rule_dict, st)

    # Fill the table cells representing substrings of length >=2
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length
            fill_cell(table, i, j, rule_dict)

    return start_var in table[0][n]


def fill_length_1_cells(table, rule_dict, st):
    n = len(st)
    for i in range(n):
        for lhs in rule_dict:  # lhs is a single variable
            if st[i] in rule_dict[lhs]:
                # add variable lhs to T[i][i+1]
                table[i][i + 1].add(lhs)


def fill_cell(table, i, j, rule_dict):
    for k in range(i + 1, j):  # non trivial partitions of s[i:j]
        for lhs in rule_dict:  # lhs is a single variable
            for rhs in rule_dict[lhs]:
                if len(rhs) == 2:  # rule like A -> XY (not like A -> a)
                    X, Y = rhs[0], rhs[1]
                    if X in table[i][k] and Y in table[k][j]:
                        table[i][j].add(lhs)


rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}

res = CYK("baaba", rule_dict, "S")
print(res)
res = CYK("baab", rule_dict, "S")
print(res)






