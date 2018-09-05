"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""
from fractions import gcd

accum = 1
top = 20

for i in range(1,top + 1):
  accum = accum * i // gcd(i, accum)

print(accum)
