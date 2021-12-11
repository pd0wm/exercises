#!/usr/bin/env python3

import numpy as np
from collections import Counter

def fill_basin(nums, basins, i, j, basin_id):
    if basins[i, j] != 0:
        return

    basins[i, j] = basin_id
    if nums[i - 1, j] != 9: fill_basin(nums, basins, i - 1, j, basin_id)
    if nums[i + 1, j] != 9: fill_basin(nums, basins, i + 1, j, basin_id)
    if nums[i, j - 1] != 9: fill_basin(nums, basins, i, j - 1, basin_id)
    if nums[i, j + 1] != 9: fill_basin(nums, basins, i, j + 1, basin_id)


nums = np.asarray([list(map(int, x.strip())) for x in open("input_09")])
nums_padded = np.pad(nums, ((1, 1), (1, 1)), constant_values=9)

basins = np.zeros_like(nums_padded)

part_01 = 0
basin_id = 0
for i, j in np.ndindex(nums.shape):
    i += 1
    j += 1
    lowest =  nums_padded[i, j] < nums_padded[i - 1, j]
    lowest &= nums_padded[i, j] < nums_padded[i + 1, j]
    lowest &= nums_padded[i, j] < nums_padded[i, j - 1]
    lowest &= nums_padded[i, j] < nums_padded[i, j + 1]
    if lowest:
        part_01 += nums_padded[i, j] + 1

        basin_id += 1
        fill_basin(nums_padded, basins, i, j, basin_id)

print(part_01)

part_02 = 1
for _, cnt in Counter([x for x in basins.flatten() if x != 0]).most_common(3):
    part_02 *= cnt
print(part_02)
