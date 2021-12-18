#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache

N = 40

@lru_cache(maxsize=None)
def count(pair, n):
    if n == 0:
        return Counter(pair[0])

    cnt = Counter()
    cnt.update(count(pair[0] + rules[pair], n - 1))
    cnt.update(count(rules[pair] + pair[1], n - 1))
    return cnt


if __name__ == '__main__':
    rules = {}

    for line in open('input_14'):
        line = line.strip()

        if ' -> ' in line:
            frm, to = line.split(' -> ')
            rules[frm] = to
        elif line == '':
            pass
        else:
            inp = line

    cnt = Counter()
    for a, b in zip(inp, inp[1:]):
        cnt.update(count(a + b, N))
    cnt.update(b)

    mc = cnt.most_common()
    print(mc[0][1] - mc[-1][1])