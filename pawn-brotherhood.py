#!/usr/bin/env python3

def safe_pawns(pawns):
    return len(list(filter(lambda pawn: any(map(lambda defence: abs(ord(pawn[0]) - ord(defence[0])) == 1 and ord(pawn[1]) - ord(defence[1]) == 1, pawns)), pawns)))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
