"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def fun(x):
    if x % 2 != 0:
        return 3*x+1
    return int(x/2)


if __name__ == "__main__":
    lengths = [0]
    for i in range(1, 1000001):
        length = 1
        while True:
            if i == 1:
                lengths.append(length)
                break
            n = fun(i)
            if n < len(lengths) - 1:
                lengths.append(lengths[n] + length)
                break
            length += 1
            i = n
    print(lengths.index(max(lengths)))
