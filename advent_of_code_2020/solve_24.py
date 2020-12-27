#!/usr/bin/env python3
import itertools
from collections import defaultdict

def get_coordinates(s):
    directions = {
        'ne': (1, -1),
        'e': (1, 0),
        'se': (0, 1),
        'sw': (-1, 1),
        'w': (-1, 0),
        'nw': (0, -1),
    }
    i = 0

    p, q = (0, 0)
    while i < len(s):
        direction = s[i]
        i += 1
        if direction in ['n', 's']:
            direction += s[i]
            i += 1

        a, b = directions[direction]
        p, q = p + a, q + b

    return (p, q)


def neighbours(t, p, q):
    r = 0
    for (dp, dq) in itertools.product((-1, 0, 1), repeat=2):
        if (dp, dq) in ((0, 0), (-1, -1), (1, 1)):
            continue
        r += t[(p + dp, q + dq)]
    return r

def step(t):
    to_set = []
    to_clear = []


    ps = [k[0] for k, v in t.items() if v]
    qs = [k[1] for k, v in t.items() if v]

    for p in range(min(ps) - 1, max(ps) + 2):
        for q in range(min(qs) - 1, max(qs) + 2):
            c = (p, q)
            n = neighbours(t, *c)
            if t[c]:
                if n == 0 or n > 2:
                    to_clear.append(c)
            elif n == 2:
                to_set.append(c)


    for c in to_set:
        t[c] = 1
    for c in to_clear:
        t[c] = 0


tiles = defaultdict(int)
with open("input_24") as f:
    for line in f:
        c = get_coordinates(line.strip())

        # Flip tile
        tiles[c] = 1 if tiles[c] == 0 else 0

print(sum(tiles.values()))

for _ in range(100):
    step(tiles)
print(sum(tiles.values()))
