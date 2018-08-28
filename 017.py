"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""
from math import floor


words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        }


def count(x):
    word = ""
    # case thousands
    if floor(x/1000) > 0:
        word += 'onethousand'
        # cheating hard
        return len(word)
    # case hundreds
    if x > 99:
        word += words[floor(x/100)] + 'hundred'
        if x % 100 > 0:
            word += 'and'
    two_digits = x-floor(x/100)*100
    if two_digits != 0:
        if two_digits not in words:
            tens = floor(two_digits/10)*10
            unit = two_digits % 10
            word += words[tens] + words[unit]
        else:
            word += words[two_digits]
    return len(word)


def sum_count(x):
    total = 0
    for i in range(1, x+1):
        total += count(i)
    return total


def test_count():
    assert(sum_count(5) == 19)
    assert(count(342) == 23)
    assert(count(115) == 20)


if __name__ == "__main__":
    print(sum_count(1000))
