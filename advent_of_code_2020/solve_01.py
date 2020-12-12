#!/usr/bin/env python3
import math
import itertools

def solve(numbers, repeat=2):
    for s in itertools.product(numbers, repeat=repeat):
        if sum(s) == 2020:
            return math.prod(s)

numbers = []
with open('input_01') as f:
    for line in f:
        numbers.append(int(line))

print(solve(numbers, 2))
print(solve(numbers, 3))
