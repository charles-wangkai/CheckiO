#!/usr/bin/env python3

def is_matching_in_a_line(matrix, r, c, offset_r, offset_c, length):
    size = len(matrix)
    
    if not (0 <= r + offset_r * (length - 1) < size and 0 <= c + offset_c * (length - 1) < size):
        return False
    
    for i in range(1, length):
        if matrix[r + offset_r * i][c + offset_c * i] != matrix[r][c]:
            return False
    return True

def checkio(matrix):
    OFFSETS = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    size = len(matrix)
    for r in range(size):
        for c in range(size):
            for offset_r, offset_c in OFFSETS:
                if is_matching_in_a_line(matrix, r, c, offset_r, offset_c, 4):
                    return True
    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
