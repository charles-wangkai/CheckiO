#!/usr/bin/env python3

import heapq

def capture(matrix):
    result = None
    computer_num = len(matrix)
    visited = [False] * computer_num
    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        time, index = heapq.heappop(pq)
        if not visited[index]:
            visited[index] = True
            result = time
            for adj in range(computer_num):
                if adj != index and not visited[adj] and matrix[index][adj]:
                    heapq.heappush(pq, (time + matrix[adj][adj], adj))
    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
