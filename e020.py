"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""
import math


if __name__ == "__main__":
    number = str(math.factorial(100))
    accum = 0
    for c in number:
        accum += int(c)
    print(accum)
