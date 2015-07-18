#!/usr/bin/env python3

def is_line_filled(game_result, player, r, c, dr, dc):
    return all([game_result[r + dr * i][c + dc * i] == player for i in range(3)])

def checkio(game_result):
    LINES = [(0, 0, 0, 1), (1, 0, 0, 1), (2, 0, 0, 1), (0, 0, 1, 0), (0, 1, 1, 0), (0, 2, 1, 0), (0, 0, 1, 1), (0, 2, 1, -1)]
    for player in ['X', 'O']:
        if any(filter(lambda line: is_line_filled(game_result, player, *line), LINES)):
            return player
    return 'D'

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
