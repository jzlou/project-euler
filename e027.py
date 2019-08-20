"""
Problem 27
==========

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
from utils import is_prime
from time import time


def quad(a, b, n):
    return n * n + a * n + b


def longest_quad(a_lim, b_lim):
    longest = (0, 0, 0)
    for a in range((a_lim*-1)+1, a_lim):
        # b must be prime in the case that n = 0
        for b in range(2, b_lim):
            if is_prime(b):
                n, count = 0, 0
                while is_prime(quad(a, b, n)):
                    count += 1
                    n += 1
                if count > longest[2]:
                    longest = (a, b, count)
    return longest


if __name__ == "__main__":
    now = time()
    top = longest_quad(1000, 1000)
    print(f"product: {top[0]*top[1]}, prime length: {top[2]}")
    print(f"took: {time() - now} seconds")
