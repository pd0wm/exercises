#!/usr/bin/env python3

import numpy as np

def filter_list(inputs, upper=True):
    N = inputs.shape[1]
    nums = inputs.copy()

    for n in range(N):
        column = nums[:, n]
        ratio = np.sum(column) / nums.shape[0]
        if bool(ratio >= 0.5) == upper:
            nums = nums[column > 0.5]
        else:
            nums = nums[column < 0.5]

        if len(nums) == 1:
            break

    x = "".join(str(x) for x in nums[0])
    return int(x, 2)


inputs = np.asarray([list(map(int, list(n.strip()))) for n in open("input_03")])
N = inputs.shape[1]

gamma = 0
epsilon = 0
for n in range(N):
    ratio = np.sum(inputs[:, N - n - 1]) / inputs.shape[0]
    if ratio > 0.5:
        gamma += 2**n
    else:
        epsilon += 2**n
print(gamma * epsilon)

print(filter_list(inputs) * filter_list(inputs, False))