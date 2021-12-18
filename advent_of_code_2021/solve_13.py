#!/usr/bin/env python3
import numpy as np

def print_grid(grid):
    for y in range(grid.shape[0]):
        print("".join('#' if x else '_' for x in grid[y]))
    print()

xs = []
ys = []

part_one = None

for line in  open('input_13'):
    line = line.strip()
    if line.startswith('fold'):
        xy = int(line.split('=')[1])

        if 'x' in line:
            left = grid[:, :xy]
            right = grid[:, xy + 1:]

            new_width = max(left.shape[1], right.shape[1])
            left = np.pad(left, ((0, 0), (new_width - left.shape[1], 0)))
            right = np.pad(right, ((0, 0), (0, new_width - right.shape[1])))
            grid = np.logical_or(left, np.fliplr(right))
        else:
            upper = grid[:xy, :]
            lower = grid[xy + 1:, :]

            new_height = max(upper.shape[0], lower.shape[0])
            upper = np.pad(upper, ((new_height - upper.shape[0], 0), (0, 0)))
            lower = np.pad(lower, ((0, new_height - lower.shape[0]), (0, 0)))
            grid = np.logical_or(upper, np.flipud(lower))

        if part_one is None:
            part_one = np.sum(grid)
    elif line == '':
        grid = np.zeros((max(ys) + 1, max(xs) + 1))
        for x, y in zip(xs, ys):
            grid[y, x] = 1
        grid = grid > 0
    else:
        x, y = [int(x) for x in line.split(',')]
        xs.append(x)
        ys.append(y)

print(part_one)
print_grid(grid)



