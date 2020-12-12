#!/usr/bin/env python3
import math
import itertools

def solve(numbers, repeat=2):
    for s in itertools.product(numbers, repeat=repeat):
        if sum(s) == 2020:
            return math.prod(s)

with open('input_01') as f:
    numbers = [int(l) for l in f]

print(solve(numbers, 2))
print(solve(numbers, 3))
