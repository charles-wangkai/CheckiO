#!/usr/bin/env python3

import functools

class Friends:
    def __init__(self, connections):
        self.connections = set(map(frozenset, connections))

    def add(self, connection):
        if frozenset(connection) in self.connections:
            return False
        
        self.connections.add(frozenset(connection))
        return True

    def remove(self, connection):
        if frozenset(connection) not in self.connections:
            return False
        
        self.connections.remove(frozenset(connection))
        return True

    def names(self):
        return functools.reduce(lambda result, connection: result | connection, self.connections, set())

    def connected(self, name):
        return functools.reduce(lambda result, connection: result | connection, filter(lambda connection: name in connection, self.connections), set()) - set([name])



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
