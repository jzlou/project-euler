"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


if __name__ == "__main__":
    i = str(2**1000)
    print(sum(int(c) for c in i))
