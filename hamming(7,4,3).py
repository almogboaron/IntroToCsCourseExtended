def hamming_encode(x3,x5,x6,x7):
    """ Hamming encoding of the 4 bits input """
    x1= (x3+x5+x7) % 2
    x2= (x3+x6+x7) % 2
    x4= (x5+x6+x7) % 2
    return (x1,x2,x3,x4,x5,x6,x7)

def hamming_decode(y1,y2,y3,y4,y5,y6,y7):
    """ Hamming decoding of the 7 bits signal """
    b1= (y1+y3+y5+y7) % 2
    b2= (y2+y3+y6+y7) % 2
    b3= (y4+y5+y6+y7) % 2
    b=4*b3+2*b2+b1  # the integer value
    if b==0:  # no error
        return (y3,y5,y6,y7)
    else:
        y=[y1,y2,y3,y4,y5,y6,y7]
        y[b-1]=(y[b-1]+1) % 2  # correct bit b
        return (y[2],y[4],y[5],y[6])









