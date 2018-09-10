from math import ceil


def proper_divisors(x):
    # returns a list of all proper divisors of x
    divisors = []
    for i in range(1, ceil(x/2)+1):
        if (x % i) == 0:
            divisors.append(i)
    return divisors


def test_proper_divisors():
    assert(proper_divisors(12) == [1, 2, 3, 4, 6])
    assert(proper_divisors(284) == [1, 2, 4, 71, 142])
    assert(proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])
