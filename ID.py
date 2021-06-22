def is_valid_ID():
    # prompts for input from user
    ID = input("pls type all 9 digits (left to right) of your ID: ")
    assert len(ID) == 9
    if control_digit(ID[:-1]) == ID[-1]:
        print("Valid ID number")
    else:
        print("ID number is incorrect")


def control_digit1(ID):
    """ compute the check digit in an Israeli ID number """

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


def string_to_list(string):
    """ converts a string of digits to a list of integers """
    digits = []
    for ch in string:
        digits += [int(ch)]
    return digits


def control_digit(ID):
    """ compute the check digit in an Israeli ID number """
    digits = string_to_list(ID)
    for i in range(8):
        if i % 2 == 1:
            temp = digits[i] * 2
            if temp < 10:
                digits[i] = temp
            else:
                digits[i] = 1 + (temp % 10)
    total = sum(digits)
    if total % 10 == 0:
        check_digit = 0
    else:
        check_digit = 10 - (total % 10)
    return str(check_digit)


is_valid_ID()

