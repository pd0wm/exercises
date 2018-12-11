#!/usr/bin/env python2

import numpy as np

n = list(range(301))
x, y = np.meshgrid(n, n)

serial = 6392
# serial = 18


rack_id = x + 10
power_level = rack_id * y + serial
power_level *= rack_id
power_level = np.floor(power_level / 100.) % 10.
power_level -= 5


max_power = 0

for n in range(300):
    print n
    for x in range(301 - n):
        for y in range(301 - n):
            power = np.sum(power_level[y:y+n, x:x+n])

            if power > max_power:
                max_power = power
                max_pos = (x, y, n)
                print max_pos

print max_power, max_pos
