"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from functools import reduce


def calculate_triple(n):
    # n is target
    for a in range(1, n):
        for b in range(1, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return (a, b, c)
    return None


def test_triple():
    assert(calculate_triple(12) == (3, 4, 5))


if __name__ == "__main__":
    print(reduce(lambda x, y: x*y, calculate_triple(1000)))
