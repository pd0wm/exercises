#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d


def step(nums):
    flashed = np.zeros_like(nums)
    nums += 1

    while np.sum(np.logical_and(nums > 9, np.logical_not(flashed))):
        to_flash = np.logical_and(nums > 9, np.logical_not(flashed))

        to_increase = convolve2d(to_flash, np.ones((3,3), dtype=np.int64), mode='same')
        nums += to_increase

        flashed = np.logical_or(to_flash, flashed)

    nums[flashed > 0] = 0
    return nums, np.sum(flashed > 0)


if __name__ == "__main__":
    nums = np.asarray([list(map(int, line.strip())) for line in open("input_11")])


    part_01 = 0
    for i in range(1000):
        nums, flashes = step(nums)

        if i < 100:
            part_01 += flashes

        if flashes == 100:
            print(part_01)
            print(i + 1)
            break
