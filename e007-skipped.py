"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import itertools


def find_primes():
    ans = next(
      itertools.islice(
        filter(
          is_this_prime,
          itertools.count(2)),
        10000,
        None)
      )
    return str(ans)


def is_this_prime():
    # make a prime-ness check
    return


def compute():
    return


if __name__ == "__main__":
    print(compute())
