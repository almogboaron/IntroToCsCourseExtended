import random
import math

def rand_walk(steps, show=False):
    pos = 0
    for i in range(steps):
        walk = random.choice([+1,-1])
        pos += walk
        if show:
             print("step", i, ":", pos)
    return pos


def test_rand_walk_dist(steps, num_simulations):
    dist = 0
    for i in range(num_simulations):
        dist += abs(rand_walk(steps))
    avg = dist/num_simulations
    return avg/(steps**0.5) #tends to (2/math.pi)**0.5

