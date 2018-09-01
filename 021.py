"""
Project Euler Problem 21
========================

Let d(n) be defined as the sum of proper divisors of n (numbers less than
n which divide evenly into n).
If d(a) = b and d(b) = a, where a =/= b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import ceil


def spd(x):
    # sum of proper divisors of x
    return sum(pd(x))


def pd(x):
    # returns list of proper divisors of x
    divisors = []
    for i in range(1, ceil(x/2)+1):
        if (x % i) == 0:
            divisors.append(i)
    return divisors


def are_amicable(x, y):
    if spd(x) == y:
        if spd(y) == x:
            return True
    return False


def test_proper_divisors():
    pd_284 = [1, 2, 4, 71, 142]
    pd_220 = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    assert(sorted(pd(284)) == pd_284)
    assert(sorted(pd(220)) == pd_220)


def test_sum_proper_divisors():
    assert(spd(220) == 284)
    assert(spd(284) == 220)


def test_are_amicable():
    assert(are_amicable(220, 284))
    assert(not are_amicable(3, 10))


if __name__ == "__main__":
    amicables = set()
    for i in range(10000):
        calc = spd(i)
        if are_amicable(i, calc):
            amicables.add(i)
            amicables.add(calc)
    print(sum(amicables))
