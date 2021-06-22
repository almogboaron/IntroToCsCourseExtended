import random

def estimate_Pi(sample_size=1000):
    count = 0
    for n in range(sample_size):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            count += 1 #inside circle
    return 4*count/sample_size



