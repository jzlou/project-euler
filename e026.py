"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""


def test_unit_frac():
    assert(unit_frac_cycle(2) == 0)
    assert(unit_frac_cycle(3) == 1)
    assert(unit_frac_cycle(4) == 0)
    assert(unit_frac_cycle(5) == 0)
    assert(unit_frac_cycle(6) == 1)
    assert(unit_frac_cycle(7) == 6)
    assert(unit_frac_cycle(8) == 0)
    assert(unit_frac_cycle(9) == 1)
    assert(unit_frac_cycle(10) == 0)


def unit_frac_cycle(i):
    if not isinstance(i, int):
        raise TypeError('expecting an int and did not.')
    if i == 0:
        return 0
    s_i = format(1/i, '.54f')


if __name__ == "__main__":
    x, longest_cycle = 0, 0
    for i in range(1000):
        cycle_length = unit_frac_cycle(i)
        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            x = i
    print(x)
