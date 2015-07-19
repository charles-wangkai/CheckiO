#!/usr/bin/env python3

def add_adjacent(adjacents, from_person, to_person):
    if from_person not in adjacents:
        adjacents[from_person] = []
    adjacents[from_person].append(to_person)

def is_friend(adjacents, person, target, visited):
    if person == target:
        return True
    
    visited.add(person)
    for adjacent in adjacents[person]:
        if adjacent not in visited:
            if is_friend(adjacents, adjacent, target, visited):
                return True
    visited.remove(person)
    return False

def check_connection(network, first, second):
    adjacents = {}
    for connection in network:
        person1, person2 = connection.split('-')
        add_adjacent(adjacents, person1, person2)
        add_adjacent(adjacents, person2, person1)
    return is_friend(adjacents, first, second, set())

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
