#!/usr/bin/env python3

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    
    max_sums = [0]
    for line in pyramid:
        next_max_sums = [max_sums[0] + line[0]]
        for i in range(1, len(line) - 1):
            next_max_sums.append(max(max_sums[i - 1], max_sums[i]) + line[i])
        if len(line) > 1:
            next_max_sums.append(max_sums[-1] + line[-1])
        max_sums = next_max_sums
    return max(max_sums)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
