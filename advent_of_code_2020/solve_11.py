#!/usr/bin/env python3
import copy
import itertools


def get_adjacent(seats, i, j):
    r = []

    for (a, b) in itertools.product((-1, 0, 1), repeat=2):
        if (a, b) == (0, 0):
            continue

        ii = i + a
        jj = j + b

        if ii < 0 or jj < 0 or ii >= len(seats) or jj >= len(seats[0]):
            continue

        r.append(seats[ii][jj])
    return r


def get_inline(seats, i, j):
    r = []

    for (a, b) in itertools.product((-1, 0, 1), repeat=2):
        if (a, b) == (0, 0):
            continue

        ii = i
        jj = j
        while True:
            ii += a
            jj += b

            if ii < 0 or jj < 0 or ii >= len(seats) or jj >= len(seats[0]):
                break

            c = seats[ii][jj]
            if c == '#':
                r.append(c)
                break
            if c == 'L':
                break

    return r


def step(seats, look, max_adj):
    next_step = copy.deepcopy(seats)

    for i in range(len(seats)):
        for j in range(len(seats[0])):
            seen = look(seats, i, j)
            c = seats[i][j]

            if c == 'L' and seen.count('#') == 0:
                next_step[i][j] = '#'
            if c == '#' and seen.count('#') >= max_adj:
                next_step[i][j] = 'L'
    return next_step


def iterate(seats, look=get_adjacent, max_adj=4):
    s = copy.deepcopy(seats)

    while True:
        n = step(s, look, max_adj)
        if n == s:
            break
        s = n

    return sum([x.count('#') for x in s])


if __name__ == "__main__":
    with open('input_11') as f:
        seats = [list(l.strip()) for l in f]

    print(iterate(seats))
    print(iterate(seats, get_inline, 5))
