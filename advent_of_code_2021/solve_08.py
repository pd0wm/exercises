#!/usr/bin/env python3
from itertools import permutations

LETTERS = 'abcdefg'
OPTIONS = [
    'abcefg',  # 0
    'cf',      # 1
    'acdeg',   # 2 
    'acdfg',   # 3
    'bcdf',    # 4
    'abdfg',   # 5
    'abdefg',  # 6
    'acf',     # 7
    'abcdefg', # 8
    'abcdfg',  # 9
]

def transform(perm, pattern):
    return ''.join(sorted([LETTERS[perm.index(c)] for c in pattern]))

if __name__ == "__main__":
    part_01 = 0
    part_02 = 0

    for line in open('input_08'):
        patterns, outputs = line.strip().split(' | ')
        patterns, outputs = patterns.split(), outputs.split()

        # Part 1
        for o in outputs:
            if len(o) in [2, 4, 3, 7]: # 1, 4, 7, 8
                part_01 += 1

        # Part 2 - Brute force all possible permutations and check if match
        for perm in  [''.join(p) for p in permutations(LETTERS)]:
            transformed = [transform(perm, p) for p in patterns]
            if all(t in OPTIONS for t in transformed):
                break

        part_02 += int(''.join([str(OPTIONS.index(transform(perm, o))) for o in outputs]))

    print(part_01)
    print(part_02)
