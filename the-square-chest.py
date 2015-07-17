#!/usr/bin/env python3

def to_number(r, c):
    return r * 4 + c + 1

def is_square(lines, size, r, c):
    return all([(to_number(r, c + i), to_number(r, c + i + 1)) in lines and (to_number(r + i, c), to_number(r + i + 1, c)) in lines and (to_number(r + size , c + i), to_number(r + size , c + i + 1)) in lines and (to_number(r + i , c + size), to_number(r + i + 1, c + size)) in lines for i in range(size)])

def checkio(lines_list):
    """Return the quantity of squares"""
    
    lines = set()
    for line in lines_list:
        lines.add((min(line), max(line)))
    
    square_num = 0
    for size in range(1, 4):
        for r in range(4 - size):
            for c in range(4 - size):
                if is_square(lines, size, r, c):
                    square_num += 1
    return square_num

if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
