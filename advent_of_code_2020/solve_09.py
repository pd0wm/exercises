#!/usr/bin/env python3

import itertools

N = 25

with open('input_09') as f:
    numbers = [int(x) for x in f]


for i in range(N, len(numbers)):
    preamble = numbers[i-N:i]
    combinations = list(itertools.combinations(preamble, 2))
    sums = [sum(c) for c in combinations]

    n = numbers[i]
    if n not in sums:
        break

print(n)

for i in range(0, len(numbers)):
    for j in range(i+2, len(numbers)):
        rng = numbers[i:j]
        if sum(rng) == n:
            print(min(rng) + max(rng))
