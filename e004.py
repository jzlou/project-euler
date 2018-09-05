"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x):
    n = str(x)
    if n == n[::-1]:
        return True
    return False


prod = 0
largest_prod = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        if is_palindrome(prod) and prod > largest_prod:
            largest_prod = prod

print(largest_prod)
