#!/usr/bin/env python3
import operator
import functools

with open('input_06') as f:
    groups = [[set(ll) for ll in l.split('\n')] for l in f.read().split('\n\n')]

total1 = 0
total2 = 0
for group in groups:
    total1 += len(functools.reduce(operator.or_, group))
    total2 += len(functools.reduce(operator.and_, group))

print(total1)
print(total2)
