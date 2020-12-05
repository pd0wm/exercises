#!/usr/bin/env python3

rows = []
with open('input_03') as f:
    for line in f:
        rows.append(line.strip())

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

r = 1
for slope_x, slope_y in slopes:
    pos_x = 0
    trees = 0
    for i in range(0, len(rows), slope_y):
        if rows[i][pos_x] == "#":
            trees += 1
        pos_x = (pos_x + slope_x) % len(rows[i])

    if (slope_x, slope_y) == (3, 1):
        print(trees)
    r *= trees

print(r)
