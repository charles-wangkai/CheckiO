#!/usr/bin/env python3

import itertools

def checkio(time_string):
    return ' : '.join(itertools.starmap(lambda number, lengths: ' '.join(itertools.starmap(lambda digit, length: ''.join(map(lambda bin_digit: {'0': '.', '1': '-'}[bin_digit], ('{digit:0' + str(length) + 'b}').format(digit=int(digit)))), zip(number, lengths))), zip(map(lambda s: '{number:02d}'.format(number=int(s)), time_string.split(':')), ((2, 4), (3, 4), (3, 4)))))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

