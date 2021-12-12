#!/usr/bin/env python3
from copy import copy
from collections import defaultdict
from os import path

def get_paths(m, allow_twice=None):
    done_paths = []
    paths = [['start']]

    while paths:
        p = paths.pop()

        if p[-1] == 'end':
            done_paths.append(p)
            continue

        for tt in m[p[-1]]:
            max_visits = 2 if (tt == allow_twice) else 1
            if tt.islower() and p.count(tt) == max_visits:
                continue

            paths.append(p + [tt])

    done_paths = [','.join(p) for p in done_paths]
    return done_paths


if __name__ == "__main__":
    # Build ajency matrix
    m = defaultdict(list)
    for line in open('input_12'):
        frm, to = line.strip().split('-')
        m[frm].append(to)
        m[to].append(frm)

    # Part 1
    paths = get_paths(m)
    print(len(paths))

    # Part 2
    lower = set([frm for frm in m.keys() if frm.islower()])
    lower -= {'start', 'end'}
    for t in lower:
        paths += get_paths(m, allow_twice=t)
    print(len(set(paths)))
