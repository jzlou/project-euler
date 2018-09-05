"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math

def smallest_prime_factor(n):
  assert n >= 2
  for i in range(2, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
      # print("found a factor: " + str(i))
      return i
  # print("found a prime: " + str(n))
  return n

def prime_factor(n):
  factors = []
  while True:
    p = smallest_prime_factor(n)
    if p < n:
      factors.append(p)
      n = n / p
    else:
      factors.append(n)
      break
  return factors

print(int(prime_factor(600851475143).pop()))
