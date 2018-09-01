"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

from datetime import date
from datetime import timedelta


def test_day_of_week():
    # monday
    assert(date(1900, 1, 1).weekday() == 0)
    # sunday
    assert(date(1900, 1, 7).weekday() == 6)


if __name__ == "__main__":
    current_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    count = 0
    while current_date <= end_date:
        if current_date.day == 1:
            if current_date.weekday() == 6:
                count += 1
        current_date += timedelta(days=1)
    print(count)
