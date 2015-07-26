#!/usr/bin/env python3

import functools

def checkio(number):
    return functools.reduce(lambda x, y: x * y, filter(lambda x: x, map(int, str(number))))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
