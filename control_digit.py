def control_digit(ID):
    """ compute the check digit in an Israeli ID number,
        given as a string """

    total = 0
    for i in range(8):
        val = int(ID[i])  # converts a char to its numeric integer value
        if i % 2 == 0:
            total = total + val
        else:
            if val < 5:
                total += 2 * val
            else:
                total += (2 * val % 10) + 1  # sum of digits in 2*val
    total = total % 10
    check_digit = (10 - total) % 10  # the complement mod 10 of sum

    return str(check_digit)



