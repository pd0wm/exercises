#!/usr/bin/env python3

import numpy as np

nums = [int(n) for n in open("input_01")]
windows = np.convolve(nums, np.ones(3), 'valid')

print(np.sum(np.diff(nums) > 0))
print(np.sum(np.diff(windows) > 0))