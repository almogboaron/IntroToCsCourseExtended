def rec_binary_search(lst, key, left, right):
    """ recursive binary search.
        passing lower and upper boundaries"""
    if left > right:
        return None

    middle = (left + right) // 2
    if key == lst[middle]:
        return middle
    elif key < lst[middle]:  # item cannot be in top half
        return rec_binary_search(lst, key, left, middle - 1)
    else:  # item cannot be in bottom half
        return rec_binary_search(lst, key, middle + 1, right)


def rec_display_binary_search(lst, key, left, right):
    """ recursive binary search.
        printing intermediate values to track execution """
    if left > right:
        return None

    middle = (left + right) // 2

    print("left=", left, "middle=", middle, "right=", right)
    print("middle element=", lst[middle])

    if key == lst[middle]:
        return middle
    elif key < lst[middle]:  # item cannot be in top half
        return rec_display_binary_search(lst, key, left, middle - 1)
    else:  # item cannot be in bottom half
        return rec_display_binary_search(lst, key, middle + 1, right)


def env_binary_search(lst, key):
    """ calls a recursive binary search
        lst better be sorted for binary search to work"""
    n = len(lst)
    return rec_binary_search(lst, key, 0, n - 1)

