#!/usr/bin/env python3

def generate_key(word):
    return ''.join(sorted(word.lower().replace(' ', '')))

def verify_anagrams(first_word, second_word):
    return generate_key(first_word) == generate_key(second_word)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

