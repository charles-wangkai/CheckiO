#!/usr/bin/env python3

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    words = []
    
    hundred = number // 100
    if hundred:
        words.append(FIRST_TEN[hundred - 1])
        words.append(HUNDRED)
    
    ten = number % 100 // 10
    one = number % 10
    if ten == 1:
        words.append(SECOND_TEN[one])
    else:
        if ten:
            words.append(OTHER_TENS[ten - 2])
        if one:
            words.append(FIRST_TEN[one - 1])
    
    return ' '.join(words)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
