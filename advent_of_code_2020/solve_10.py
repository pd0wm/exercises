#!/usr/bin/env python3
import numpy as np

tri = [1, 1, 2, 4]
for _ in range(100):
    n = len(tri)
    tri.append(tri[n - 1] + tri[n - 2] + tri[n - 3])

with open('input_10') as f:
    numbers = [int(x) for x in f]

dev = max(numbers) + 3
numbers.append(dev)
numbers.append(0)

numbers = sorted(numbers)
d = np.diff(numbers)

# Q1
print(np.sum(d == 1) * np.sum(d == 3))

# Q2
r = 1
c = 0
for i in d:
    if i == 3:
        r *= tri[c]
        c = 0
    else:
        c += 1

print(r)
