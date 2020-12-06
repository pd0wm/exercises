#!/usr/bin/env python3
import operator
import functools

with open('input_06') as f:
    groups = [[set(ll) for ll in l.split('\n')] for l in f.read().split('\n\n')]

print(sum([len(functools.reduce(operator.or_, g)) for g in groups]))
print(sum([len(functools.reduce(operator.and_, g)) for g in groups]))
