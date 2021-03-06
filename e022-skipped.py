"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""
from functools import reduce


def calculate_value(name):
    return reduce(lambda x, y: x+y, [ord(c)-ord('A')+1 for c in name.upper()])


def load_sorted_data(loc="resources/names.txt"):
    with open(loc) as file:
        raw = file.read()
    return sorted(raw.split(','))


def test_calculate_value():
    assert(calculate_value('COLIN')*938 == 49714)


def test_data_load():
    data = load_sorted_data()
    print(data.__name__)
    assert(data.index('COLIN') == 938-1)


if __name__ == "__main__":
    accum = 0
    for i, datum in enumerate(load_sorted_data()):
        accum += (i+1)*calculate_value(datum)
    print(accum)
