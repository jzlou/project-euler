from math import ceil, sqrt


def proper_divisors(x):
    # returns a list of all proper divisors of x
    divisors = []
    for i in range(1, ceil(x/2)+1):
        if (x % i) == 0:
            divisors.append(i)
    return divisors


def test_proper_divisors():
    assert proper_divisors(12) == [1, 2, 3, 4, 6]
    assert proper_divisors(284) == [1, 2, 4, 71, 142]
    assert proper_divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]


# borrowed algorithm, TODO: implement atkin sieve
def is_prime(n):
    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(8821)
    assert not is_prime(75531)
