"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""
from itertools import permutations


def test_lex_order():
    perms = lex_perm([0, 1, 2])
    assert(perms == ['012', '021', '102', '120', '201', '210'])


def lex_perm(ins):
    """
    takes an array of inputs
    returns an array of permutations in lexicographical order
    """
    s_ins = sorted(ins)
    # permutation returns a list of tuples, so we need to make a string
    return [''.join(str(x) for x in y) for y in permutations(s_ins)]


if __name__ == "__main__":
    print(lex_perm(list(range(10)))[999999])
