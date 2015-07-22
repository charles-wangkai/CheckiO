#!/usr/bin/env python3

def checkio(words):
    word_list = words.split()
    return any(map(lambda i: all(map(lambda j: word_list[j].isalpha(), range(i, i + 3))), range(len(word_list) - 2)))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
