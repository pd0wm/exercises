#!/usr/bin/env python3
import math
import cmath

DIRS = {
    'N': 1j,
    'S': -1j,
    'E': 1,
    'W': -1,
}

def movement(d, a):
    if d in DIRS:
        return a * DIRS[d]
    else:
        return 0

def step(ship, wp, instruction, move_ship=True):
    d = instruction[0]
    a = int(instruction[1:])

    if move_ship:
        ship += movement(d, a)
    else:
        wp += movement(d, a)

    if d == 'L':
        wp *= cmath.exp(1j * math.radians(a))
    elif d == 'R':
        wp *= cmath.exp(1j * math.radians(-a))
    elif d == 'F':
        ship += a * wp

    return ship, wp


if __name__ == "__main__":
    with open('input_12') as f:
        rows = [x.strip() for x in f]

    for wp, move_ship in ((1 + 0j, True), (10 + 1j, False)):
        ship = 0 + 0j
        for r in rows:
            ship, wp = step(ship, wp, r, move_ship)
        print(round(abs(ship.real) + abs(ship.imag)))
