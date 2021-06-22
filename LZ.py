import math, urllib.request, time

########################
# toy examples of texts
########################

s = "aaabbbaaabbbaaa"

text = """how much wood would the wood chuck chuck if the wood chuck
would chuck wood should could hood"""


#################
# LZW code
#################

def maxmatch(T, p, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ Finds a maximum match of length k<=L within a
        W long window, T[p:p+k] = T[p-m:p-m+k].
        Returns m (offset) and k (match length) """
    assert isinstance(T, str)
    n = len(T)
    m = 0
    k = 0
    for offset in range(1, 1 + min(p, W)):
        match_len = 0
        j = p - offset  # starting point of earlier repetition
        while match_len < min(n - p, L) and T[j + match_len] == T[p + match_len]:
            match_len += 1  # at this point, T[j:j+match_len]==T[p:p+match_len]
        if match_len > k:
            k = match_len
            m = offset
    return m, k  # returned offset is smallest one (closest to p)
    # among all max matches


def LZW_compress(text, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ LZW compression of an ascii text. Produces
        a list comprising of either ascii characters
        or pairs [m,k] where 1<=m<=W is an offset and
        3<=k<=L is a match """
    intermediate = []
    n = len(text)
    p = 0
    while p < n:
        m, k = maxmatch(text, p, W, L)
        if k <= 2:
            intermediate.append(text[p])  # a single char
            p += 1
        else:  # k>=3
            intermediate.append([m, k])  # compressing 3+ characters
            p += k
    return intermediate  # a list composed of chars and pairs


def LZW_decompress(intermediate):
    """ LZW decompression from intermediate format to ascii text"""
    text_lst = []
    for i in range(len(intermediate)):
        if type(intermediate[i]) == str:  # char, as opposed to a pair [m,k]
            text_lst.append(intermediate[i])
        else:
            m, k = intermediate[i]
            for j in range(k):  # append k times to result
                text_lst.append(text_lst[-m])
                # a fixed offset m "to the left", as result itself grows
    return "".join(text_lst)


def inter_to_bin(intermediate, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ converts intermediate format compressed list
        to a string of bits"""
    W_width = math.floor(math.log(W, 2)) + 1
    L_width = math.floor(math.log(L, 2)) + 1
    bits = []
    for elem in intermediate:
        if type(elem) == str:
            bits.append("0")  # to note a single char ahead
            bits.append((bin(ord(elem))[2:]).zfill(7))
        else:  # elem is a list [m,k]
            bits.append("1")  # to note a repetition ahead
            m, k = elem
            bits.append((bin(m)[2:]).zfill(W_width))
            bits.append((bin(k)[2:]).zfill(L_width))
    return "".join(ch for ch in bits)


def bin_to_inter(bits, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ converts a compressed string of bits
       to intermediate compressed format """
    W_width = math.floor(math.log(W, 2)) + 1
    L_width = math.floor(math.log(L, 2)) + 1
    inter = []
    n = len(bits)
    p = 0
    while p < n:
        if bits[p] == "0":  # single ascii char ahead (next 7 bits)
            p += 1
            char = chr(int(bits[p:p + 7], 2))
            inter.append(char)
            p += 7
        elif bits[p] == "1":  # repeat [m,k] ahead
            p += 1
            m = int(bits[p:p + W_width], 2)
            p += W_width
            k = int(bits[p:p + L_width], 2)
            p += L_width
            inter.append([m, k])
    return inter


#########################
### Various examples
#########################

def process(text):
    """ packages the whole process using LZW compression """
    inter = LZW_compress(text)
    bits = inter_to_bin(inter)
    inter2 = bin_to_inter(bits)
    text2 = LZW_decompress(inter)
    return inter, bits, inter2, text2


def str_to_ascii(text):
    """ Gets rid of non ascii characters in text"""
    return ''.join(ch for ch in text if ord(ch) < 128)

#######
### NYT
#######

##url = 'http://www.nytimes.com'
##nyt = urllib.request.urlopen(url).read().decode('utf-8')
##asci_nyt = str_to_ascii(nyt)
##inter, bits, inter2, text2 = process(asci_nyt)
##print("len of uncompressed ascii text:", len(asci_nyt)*7)
##print("len of compressed text:", len(bits))
##print("Compression ratio:", len(bits) / len(asci_nyt)*7)
##print(text2 == asci_nyt) #should be True


#######################
### Cholera proteome
#######################

##cholera = open("Vibrio_cholerae_B33.txt").read()
##print("Cholera proteome length: ", len(cholera))
##t1 = time.time()
##inter, bits, inter2, text2 = process(cholera)
##t2 = time.time()
##assert text2 == cholera # sanity check
##print(t2-t1)
##print("Cholera proteome compression ratio: ", len(bits)/(7*len(cholera)),"\n")



