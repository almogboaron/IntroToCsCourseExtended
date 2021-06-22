def add(bin1, bin2):
    maxzeros = max(len(bin1),len(bin2))
    bin1 = bin1.zfill(maxzeros)
    bin2 = bin2.zfill(maxzeros)
    result = ""
    carry = False
    for b1,b2 in zip(bin1[::-1],bin2[::-1]):
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
    return result