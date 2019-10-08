"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""
from functools import reduce


def test_is_sum_powers():
    assert(is_sum_power(1634, 4))
    assert(not is_sum_power(1645, 4))
    assert(is_sum_power(8208, 4))
    assert(is_sum_power(9474, 4))


def is_sum_power(n, p):
    i = reduce(lambda x, y: int(x) + int(y) ** p, f"0{n}")
    if i == n:
        return True
    return False


if __name__ == "__main__":
    accum = 0
    for i in range(2, 1000000):
        if is_sum_power(i, 5):
            accum += i
    print(accum)
