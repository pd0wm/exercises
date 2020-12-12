#!/usr/bin/env python3
import math
import cmath

with open('input_12') as f:
    rows = [x.strip() for x in f]

# Part 1
ship = 0 + 0j
wp = 1 + 0j

for r in rows:
    d = r[0]
    a = int(r[1:])

    if d == 'N':
        ship += 1j * a
    elif d == 'S':
        ship -= 1j * a
    elif d == 'E':
        ship += a
    elif d == 'W':
        ship -= a
    elif d == 'L':
        wp = wp * cmath.exp(1j * math.radians(a))
    elif d == 'R':
        wp = wp * cmath.exp(1j * math.radians(-a))
    elif d == 'F':
        ship += a * wp

x = abs(ship.real) + abs(ship.imag)
print(round(x))

# Part 2
ship = 0 + 0j
wp = 10 + 1j

for r in rows:
    d = r[0]
    a = int(r[1:])

    if d == 'N':
        wp += 1j * a
    elif d == 'S':
        wp -= 1j * a
    elif d == 'E':
        wp += a
    elif d == 'W':
        wp -= a
    elif d == 'L':
        wp = wp * cmath.exp(1j * math.radians(a))
    elif d == 'R':
        wp = wp * cmath.exp(1j * math.radians(-a))
    elif d == 'F':
        ship += a * wp

x = abs(ship.real) + abs(ship.imag)
print(round(x))
