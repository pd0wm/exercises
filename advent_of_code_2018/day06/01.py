#!/usr/bin/env python2
import numpy as np

f = open('input.txt')
# f = open('input_demo.txt')

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
        min_dist = np.min(dists)
        if np.sum(dists == min_dist) == 1:
            grid[y, x] = np.argmin(dists)
        else:
            grid[y, x] = -1

mask = np.ones((m-1, m-1))
mask = np.pad(mask, ((1, 1), (1, 1)), 'constant')
mask = np.logical_not(mask)


max_area = 0
not_on_border = []
for i in range(len(coords)):
    in_border = np.sum(np.logical_and(grid == i, mask))
    if in_border == 0:
        area = np.sum(grid == i)
        if area > max_area:
            max_area = area

print max_area
