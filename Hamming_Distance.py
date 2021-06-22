def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(s1[i] != s2[i] for i in range(len(s1)))


# a decoder for a repetition code in which each bit is sent 3 times
decoder = {"000": "0", "100": "0", "010": "0", "001": "0",
           "111": "1", "011": "1", "101": "1", "110": "1"}


def decode(word, dictio=decoder):
    if word in dictio:
        return dictio[word]
    else:
        return "error"
