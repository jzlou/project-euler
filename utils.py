from math import ceil


def proper_divisors(x):
    # returns a list of all proper divisors of x
    divisors = []
    for i in range(1, ceil(x/2)+1):
        if (x % i) == 0:
            divisors.append(i)
    return divisors
