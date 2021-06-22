def float_add(a, b):
    ##deviding info
    signa, signb = a[0], b[0]
    expa, expb = int(a[1:12], 2) - 1023, int(b[1:12], 2) - 1023
    fractiona, fractionb = "1" + a[12:], "1" + b[12:]
    ##zero
    if signa!=signb and a[1:]==b[1:]:
        return "0"*64
    #checking exponent if aqual
    shift = abs(expa - expb)
    if shift != 0: #not aqual
        if expa > expb:#shifting a or b
            fractionb = "0" * shift + fractionb[:-shift]
            newexp = expa
        else:
            fractionb = "0" * shift + fractiona[:-shift]
            newexp = expb
    else: # same exponent
        newexp = expa
    if signa == signb:#both same signal which means regular addetive
        newfraction = bin((int(fractiona, 2) + int(fractionb, 2)))[2:]
        if len(newfraction) > len(fractiona):
            newexp = newexp+1
            newfraction = newfraction[:54]
            return signa + bin(newexp + 1023)[2:] + newfraction[1:]
        else:
            return signa + bin(newexp + 1023)[2:] + newfraction[1:]
    else:
        if signa == "0" and signb == "1":
            newfraction = int(fractiona,2) -int(fractionb,2)
        else:
            newfraction = int(fractionb, 2) - int(fractiona, 2)
        if newfraction < 0:
            newfraction = abs(newfraction)
            newsign = "1"
        else:
            newsign = "0"
        newfraction = bin(newfraction)[2:]
        if len(newfraction) < 53:
            newfraction = newfraction + "0" * (53 - len(newfraction))
        return newsign + bin(newexp + 1023)[2:] + newfraction[2:]
a = "0100000000000100110011001100110011001100110011001100110011001101"
b = "1011111111110110011001100110011001100110011001100110011001100110"
r = "0011111111110011001100110011001100110011001100110011001100110011"
res=float_add(a,b)
bin_to_float = lambda x: (-1)**int(x[0])*2**(int(x[1:12],2)-1023)*(1+int(x[12:],2)*2**(-52))
floata = bin_to_float(a)
floatb = bin_to_float(b)
floatc = bin_to_float(r)
floatres = bin_to_float(res)