#!/usr/bin/env python3

def dfs(matrix, visited, r, c):
    OFFSETS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    size = len(matrix)
    visited[r][c] = True
    
    group_size = 1
    for offset_r, offset_c in OFFSETS:
        next_r, next_c = r + offset_r, c + offset_c
        if 0 <= next_r < size and 0 <= next_c < size and not visited[next_r][next_c] and matrix[next_r][next_c] == matrix[r][c]:
            group_size += dfs(matrix, visited, next_r, next_c)
    return group_size

def checkio(matrix):
    size = len(matrix)
    visited = [[False] * size for _ in range(size)]
    
    max_group_size, number_for_max_group = 0, 0
    for r in range(size):
        for c in range(size):
            if not visited[r][c]:
                group_size = dfs(matrix, visited, r, c)
                if group_size > max_group_size:
                    max_group_size, number_for_max_group = group_size, matrix[r][c]
    
    return [max_group_size, number_for_max_group]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
