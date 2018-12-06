#!/usr/bin/env python2
import numpy as np

f = open('input.txt')

coords = []
for line in f:
    coords.append(map(int, line.rstrip().split(', ')))
coords = np.asarray(coords)


m = np.max(coords)
grid = np.zeros((m+1, m+1))

for x in range(m+1):
    for y in range(m+1):
        c = np.array([x, y])

        dists = np.sum(np.abs(coords - c), axis=1)
        if np.sum(dists) < 10000:
            grid[y, x] = -1

print np.sum(grid == -1)
