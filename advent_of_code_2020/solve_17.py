#!/usr/bin/env python3
from collections import defaultdict
import itertools


def neighbours(space, x, y, z, w):
    r = 0
    for (dx, dy, dz, dw) in itertools.product((-1, 0, 1), repeat=4):
        if (0, 0, 0, 0) == (dx, dy, dz, dw):
            continue
        r += space[(x + dx, y + dy, z + dz, w + dw)]
    return r


def step(space):
    to_set = []
    to_clear = []

    xs = [k[0] for k, v in space.items() if v]
    ys = [k[1] for k, v in space.items() if v]
    zs = [k[2] for k, v in space.items() if v]
    ws = [k[3] for k, v in space.items() if v]

    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            for z in range(min(zs) - 1, max(zs) + 2):
                for w in range(min(ws) - 1, max(ws) + 2):
                    c = (x, y, z, w)
                    n = neighbours(space, *c)
                    if space[c]:
                        if n not in [2, 3]:
                            to_clear.append(c)
                    if not space[c] and n == 3:
                        to_set.append(c)

    for c in to_set:
        space[c] = 1
    for c in to_clear:
        space[c] = 0

    return space



if __name__ == "__main__":
    space = defaultdict(int)

    with open('input_16') as f:
        x = 0
        y = 0
        z = 0
        w = 0
        for line in f:
            x = 0
            for c in line.strip():
                if c == '#':
                    space[(x, y, z, w)] = 1
                x += 1
            y += 1

    print(sum(space.values()))
    for _ in range(6):
        space = step(space)
        print(sum(space.values()))
