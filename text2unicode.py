def text2Unicode(text):
    ''' return a list of ints representing text '''
    lst = []
    for c in text:
        lst += [ord(c)]
    return lst

def text2bits(text):
    ''' return a string of bits representing text '''
    lst = []
    for c in text:
        lst += [bin(ord(c))[2:]]
    return "".join(lst)


