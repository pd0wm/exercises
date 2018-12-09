#!/usr/bin/env python3

inp = list(map(int, open('input.txt').read().rstrip().split()))


def parse_node(i=0):
    num_child_nodes = inp[i]
    num_metadata = inp[i+1]

    total = 0
    length = 2

    for j in range(num_child_nodes):
        s, l = parse_node(i + length)
        total += s
        length += l

    for j in range(num_metadata):
        total += inp[i + length]
        length += 1

    return total, length



print(parse_node()[0])
