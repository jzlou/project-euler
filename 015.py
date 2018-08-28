"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
from math import factorial as fac


def nCr(n, r):
    return int(fac(n) / (fac(n-r)*fac(r)))


if __name__ == "__main__":
    print(nCr(40, 20))
