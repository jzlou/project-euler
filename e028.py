"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""


def recur_spiral(prev_sum, n, target):
    if target == 1:  # base case
        return 1
    if n > target:
        print(prev_sum)
        return prev_sum
    if n == 1:
        recur_spiral(1, 3, target)
    else:
        top_right = n ** 2
        top_left = n ** 2 - n + 1
        bot_left = n ** 2 - 2 * n + 2
        bot_right = n ** 2 - 3 * n + 3
        this_sum = sum((top_right, top_left, bot_left, bot_right), prev_sum)
        recur_spiral(this_sum, n+2, target)


def test_spiral():
    """
    TODO: why doesn't this work??
    """
    assert(recur_spiral(0, 1, 5) == 101)


if __name__ == "__main__":
    recur_spiral(0, 1, 1001)
