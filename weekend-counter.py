#!/usr/bin/env python3

from datetime import date, timedelta

def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    weekend_num = 0
    delta = timedelta(days=1)
    d = from_date
    while True:
        if d.weekday() in [5, 6]:
            weekend_num += 1
        
        if d == to_date:
            break
        
        d += delta
    return weekend_num

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

