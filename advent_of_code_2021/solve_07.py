#!/usr/bin/env python3
import numpy as np

def fuel_01(inp, target):
    return np.sum(np.abs(inp - target))

def fuel_02(inp, target):
    d = np.abs(inp - target)
    return np.sum(d * (d + 1) // 2)

if __name__ == "__main__":
    inp = np.asarray([int(n) for n in open("input_07").read().split(',')])
    print(min([fuel_01(inp, t) for t in range(min(inp), max(inp) + 1)]))
    print(min([fuel_02(inp, t) for t in range(min(inp), max(inp) + 1)]))
