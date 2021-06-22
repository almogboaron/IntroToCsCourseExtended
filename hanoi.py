def HanoiTowers(start, via, target, n):
    """ computes a list of discs steps to move a stack of n discs from
    rod "start" to rod "target" employing intermediate rod "via" """
    if n > 0:
        HanoiTowers(start, target, via, n - 1)
        print("disk", n, "from", start, "to", target)
        HanoiTowers(via, start, target, n - 1)


# HanoiTowers("A", "B", "C", 3)


def hanoi_move(start, via, target, n, k):
    """ finds the k-th move in an Hanoi Towers instance
    with n discs """
    if n <= 0:
        print("zero or fewer disks")
    elif k <= 0 or k >= 2 ** n or type(k) != int:
        print("number of moves is illegal")
    elif k == 2 ** (n - 1):
        print("disk", n, "from", start, "to", target)
    elif k < 2 ** (n - 1):
        hanoi_move(start, target, via, n - 1, k)
    else:
        hanoi_move(via, start, target, n - 1, k - 2 ** (n - 1))
