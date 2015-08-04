#!/usr/bin/env python3

import math

def compute_angle(sides):
    a, b, c = sides
    return math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))

def checkio(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return [0, 0, 0]
    else:
        return sorted(map(round, map(compute_angle, [(a, b, c), (b, c, a), (c, a, b)])))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
