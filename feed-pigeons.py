#!/usr/bin/env python3

def checkio(number):
    fed_num = 0
    pigeon = 0
    minute = 1
    while number:
        number -= min(number, pigeon)
        
        extra = min(minute, number)
        fed_num += extra
        number -= extra
        
        pigeon += minute
        minute += 1
    return fed_num

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
