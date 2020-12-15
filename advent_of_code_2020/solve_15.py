#!/usr/bin/env python3
from collections import defaultdict, deque


def get_last_spoken(puzzle, N):
    spoken = defaultdict(lambda: deque(maxlen=2))

    for i, n in enumerate(puzzle):
        spoken[n].append(i)
    last_spoken = puzzle[-1]

    for i in range(len(puzzle), N):
        if len(spoken[last_spoken]) == 1:
            number = 0
        else:
            number = spoken[last_spoken][-1] - spoken[last_spoken][-2]

        spoken[number].append(i)
        last_spoken = number
    return last_spoken


puzzle = [1, 0, 18, 10, 19, 6]
print(get_last_spoken(puzzle, 2020))
print(get_last_spoken(puzzle, 30000000))
