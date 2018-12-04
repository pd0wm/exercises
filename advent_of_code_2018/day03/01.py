#!/usr/bin/env python2
import numpy as np

N = 1001

fabric = np.zeros((N, N))

inputs = []

max_x = 0
max_y = 0

for line in open('input.txt'):
    line = line.rstrip()
    line = line.split(' ')

    id = int(line[0][1:])
    pos = map(int, line[2][:-1].split(','))
    size = map(int, line[3].split('x'))
    inputs.append((id, pos, size))

    fabric[pos[1]:pos[1]+size[1], pos[0]:pos[0]+size[0]] += 1

print np.sum(fabric > 1)


for id, pos, size in inputs:
    if np.sum(fabric[pos[1]:pos[1]+size[1], pos[0]:pos[0]+size[0]] == 1) == (size[0] * size[1]):
        print id
