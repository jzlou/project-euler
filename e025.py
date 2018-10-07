"""
Project Euler Problem 25
========================

The Fibonacci sequence is defined by the recurrence relation:

  F[n] = F[n[1]] + F[n[2]], where F[1] = 1 and F[2] = 1.

Hence the first 12 terms will be:

  F[1] = 1
  F[2] = 1
  F[3] = 2
  F[4] = 3
  F[5] = 5
  F[6] = 8
  F[7] = 13
  F[8] = 21
  F[9] = 34
  F[10] = 55
  F[11] = 89
  F[12] = 144

The 12th term, F[12], is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""


def test_fib_counter():
    assert(fib_counter(3) == 12)
    assert(fib_counter(2) == 7)


def fib_counter(target_count):
    previous = 1
    current = 0
    index = 0
    while True:
        if len(str(current)) > target_count:
            raise ValueError('overshot target')
        elif len(str(current)) == target_count:
            return index
        previous, current = current, previous + current
        index += 1


if __name__ == "__main__":
    print(fib_counter(1000))
