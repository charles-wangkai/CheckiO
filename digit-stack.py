#!/usr/bin/env python3

import collections

def digit_stack(commands):
    sum = 0
    stack = collections.deque()
    for command in commands:
        if command == 'POP':
            sum += stack.pop() if stack else 0
        elif command == 'PEEK':
            sum += stack[-1] if stack else 0
        else:  # PUSH X
            stack.append(int(command.split()[1]))
    return sum

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
