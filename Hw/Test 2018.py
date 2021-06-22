def selection_sort_2(lst):
    n = len(lst)
    for i in range(n):
        m= min(lst[i:n])
        m_index = lst.index(m)
        lst[i],lst[m_index] = lst[m_index],lst[i]
        print(lst)
    return None
selection_sort_2([1,3,2,4,2])

def power1(a,b):
    bits = bin(b)[2:]
    print(bits)
    product = 1
    print(product)
    for bit in bits:
        product *= product
        if bit == "1":
            product = product * a
        print(product)
    print("\n")
    return product

power1(2,5)