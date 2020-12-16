#!/usr/bin/env python3

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def get_wait_time(busses, ts0):
    ts = ts0

    while True:
        for b in busses:
            if b == -1:
                continue
            if ts % b == 0:
                return b * (ts - ts0)

        ts += 1

if __name__ == "__main__":
    with open('input_13') as f:
        x = f.read().split('\n')

    ts = int(x[0])
    busses = [int(b) if b != 'x' else -1 for b in x[1].split(',')]
    print(get_wait_time(busses, ts))


    a = []
    n = []
    for i, b in enumerate(busses):
        if b == -1:
            continue
        a.append(b - i)
        n.append(b)

    print(chinese_remainder(n, a))
