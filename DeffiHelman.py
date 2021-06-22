import random, time

def is_prime(N, show_witness=False):
    """ probabilistic test for N's compositeness """
    for i in range(0,100):
        a = random.randint(1,N-1) # a is a random integer in [1..N-1]
        if pow(a,N-1,N) != 1:
            if show_witness:  # caller wishes to see a witness
                print(N, "is composite","\n",a,"is a witness, i=",i+1)
            return False
    return True


def find_prime(n):
    """ find random n-bit long prime """
    while(True):
        candidate = random.randrange(2**(n-1),2**n)
        if is_prime(candidate):
            return candidate


def DH_exchange():
    """ generates a shared DH key """
    n = int(input("How many bits for the prime number? "))
    p = find_prime(n)
    print("p =",p, "a large prime")
    g = random.randint(2,p-1)
    print("g =",g, "random 1<g<p")
    print()
    a = random.randint(2,p-1)# Alice's  secret
    print("a = ? random secret of Alice")
    b = random.randint(2,p-1)# Bob's  secret
    print("b = ? random secret of Bob")
    print()
    x = pow(g,a,p) #Alice's transmission
    print("x =",x, "Alice sends to Bob x = g**a%p")
    y = pow(g,b,p) #Bob's transmission
    print("y =",y, "Bob sends to Alice y = g**b%p")
    print()
    key_A = pow(y,a,p) #shared key on Alice's side
    print("key_A =", key_A, "shared key on Alice's side y**a%p")
    key_B = pow(x,b,p) #shared key on Bob's side
    print("key_B =", key_B, "shared key on Bob's side x**b%p")
    if key_A != key_B:
        print("This can't happen!", key_A, "!=", key_B)

