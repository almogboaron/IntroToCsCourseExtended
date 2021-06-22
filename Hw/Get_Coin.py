import random
def get_biased_coin(p):
    return lambda: random.random() < p

def test_biased_coin(p, num_flips):
    sumtrue = 0
    func = get_biased_coin(p)
    for i in range(num_flips):
        if func():
            sumtrue += 1
    return sumtrue/num_flips
    # 2e

if not callable(get_biased_coin(0.8)) or get_biased_coin(0.3)() not in [True, False]:
        print("error in get_biased_coin")

    # 2f
if abs(test_biased_coin(0.3, 100000) - 0.3) > 0.01:
    print("error in test_biased_coin")
