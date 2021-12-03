#!/usr/bin/env python3

import numpy as np

def one_most_common(nums, n):
    column = nums[:, n]
    ratio = np.sum(column) / nums.shape[0]
    return ratio >= 0.5

def filter_list(inputs, upper=True):
    N = inputs.shape[1]
    nums = inputs.copy()

    for n in range(N):
        if one_most_common(nums, n) == upper:
            nums = nums[nums[:, n] > 0.5]
        else:
            nums = nums[nums[:, n] < 0.5]

        if len(nums) == 1:
            break

    x = "".join(str(x) for x in nums[0])
    return int(x, 2)


if __name__ == "__main__":
    inputs = np.asarray([list(map(int, list(n.strip()))) for n in open("input_03")])
    N = inputs.shape[1]

    # Part one
    gamma = 0
    for n in range(N):
        if one_most_common(inputs, N - n - 1):
            gamma += 2**n
    epsilon = gamma ^ (2**N - 1)
    print(gamma * epsilon)

    # Part two
    print(filter_list(inputs) * filter_list(inputs, False))