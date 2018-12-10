#!/usr/bin/env python2

import numpy as np


def print_points(points):
    """Helper function to display grid of points"""
    xs = points[0, :]
    ys = points[1, :]
    pts = zip(xs, ys)

    for y in range(np.min(ys), np.max(ys) + 1):
        for x in range(np.min(xs), np.max(xs) + 1):
            if (x, y) in pts:
                print "#",
            else:
                print ".",
        print


# Read points from file
points = []
for line in open('input.txt'):
    l = line[10:].split('> v')
    vx, vy = map(int, l[1][9:-2].split(', '))
    x, y = map(int, l[0].split(', '))
    points.append([x, y, vx, vy])
points = np.asarray(points).T


# Update matrix to advance one generation
A = np.array([[1, 0, 1, 0],
              [0, 1, 0, 1],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

# Initial size
prev_size = np.prod(np.ptp(points[:2, :], axis=1))

i = 0
while True:
    new_points = A.dot(points)
    size = np.prod(np.ptp(new_points[:2, :], axis=1))

    if size > prev_size:
        break

    points = new_points
    prev_size = size
    i += 1


print_points(points)
print i
