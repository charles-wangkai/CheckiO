#!/usr/bin/env python3

def add_connection(connections, from_ring, to_ring):
    if from_ring not in connections:
        connections[from_ring] = set()
    connections[from_ring].add(to_ring)

def search(connections, ring_list, index, chosen_rings):
    if index == len(ring_list):
        return len(chosen_rings)
    
    max_chosen_num = search(connections, ring_list, index + 1, chosen_rings)
    if not (connections[ring_list[index]] & chosen_rings):
        chosen_rings.add(ring_list[index])
        max_chosen_num = max(max_chosen_num, search(connections, ring_list, index + 1, chosen_rings))
        chosen_rings.remove(ring_list[index])
    return max_chosen_num

def break_rings(rings):
    connections = {}
    for ring1, ring2 in rings:
        add_connection(connections, ring1, ring2)
        add_connection(connections, ring2, ring1)
    
    return len(connections) - search(connections, list(connections.keys()), 0, set())

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
