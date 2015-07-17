#!/usr/bin/env python3

import collections

def to_point(coord):
    return (ord(coord[0]) - ord('a'), ord(coord[1]) - ord('1'))

def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """

    OFFSETS = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    begin = to_point(cells[:2])
    end = to_point(cells[-2:])
    
    point2step = {begin: 0}
    queue = collections.deque([begin])
    while True:
        head = queue.popleft()
        
        if head == end:
            return point2step[head]
        
        for offset_r, offset_c in OFFSETS:
            next_r, next_c = head[0] + offset_r, head[1] + offset_c
            next = (next_r, next_c)
            if 0 <= next_r < 8 and 0 <= next_c < 8 and next not in point2step:
                point2step[next] = point2step[head] + 1
                queue.append(next)

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
