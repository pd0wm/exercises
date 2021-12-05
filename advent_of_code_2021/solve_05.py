#!/usr/bin/env python3

import math
import numpy as np

N = 1000

if __name__ == "__main__":
    for part_two in [False, True]:

        grid = np.zeros((N, N))
        for line in open('input_05'):
            frm, to = line.strip().split(' -> ')
            frm, to = frm.split(','), to.split(',')

            frm_x, frm_y = [int(x) for x in frm]
            to_x, to_y = [int(x) for x in to]

            straight = (frm_x == to_x) or (frm_y == to_y)
            if (not straight) and (not part_two):
                continue

            dx = to_x - frm_x
            dy = to_y - frm_y

            steps = max(abs(dx), abs(dy))
            for i in range(steps + 1):
                x = frm_x + i * dx // steps
                y = frm_y + i * dy // steps
                grid[x, y] += 1

        print(np.sum(grid >= 2))
