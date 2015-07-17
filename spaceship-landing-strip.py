#!/usr/bin/env python3

import collections

def find_largest_rectangle_in_histogram(heights):
    extended_heights = heights[:] + [0]
    
    indices = collections.deque()
    max_area = 0
    for i in range(len(extended_heights)):
        while indices and extended_heights[i] <= extended_heights[indices[-1]]:
            h = extended_heights[indices.pop()]
            max_area = max(max_area, h * (i - (indices[-1] + 1 if indices else 0)))
        indices.append(i)
    return max_area

def update_heights(heights, one_row):
    for i in range(len(heights)):
        if one_row[i]:
            heights[i] += 1
        else:
            heights[i] = 0

def find_max_rectangle(matrix):
    row, col = len(matrix), len(matrix[0])
    
    max_area = 0
    heights = [0] * col
    for i in range(row):
        update_heights(heights, matrix[i])
        max_area = max(max_area, find_largest_rectangle_in_histogram(heights))
    return max_area

def checkio(landing_map):
    row, col = len(landing_map), len(landing_map[0])
    
    island = []
    for i in range(row):
        one_row = []
        for j in range(col):
            one_row.append(landing_map[i][j] in 'GS')
        island.append(one_row)
    
    return find_max_rectangle(island)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(['G']) == 1, 'One cell - one variant'
    assert checkio(['GS',
                    'GS']) == 4, 'Four good cells'
    assert checkio(['GT',
                    'GG']) == 2, 'Four cells, but with a tree'
    assert checkio(['GGTGG',
                    'TGGGG',
                    'GSSGT',
                    'GGGGT',
                    'GWGGG',
                    'RGTRT',
                    'RTGWT',
                    'WTWGR']) == 9, 'Classic'
