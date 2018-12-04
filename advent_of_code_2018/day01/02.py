#!/usr/bin/env python2

from fractions import gcd


# Build list of frequencies
s = 0
freqs = []
for line in open('input.txt'):
    line = line.rstrip()
    if len(line):
        s += int(line)
        freqs.append(s)
fn = freqs[-1]
print "Final frequency: %d" % fn


min_pos = None
solution = None

a = fn
b = -fn
g = gcd(a, b)
for i, fi in enumerate(freqs):
    for j, fj in enumerate(freqs):
        if fi == -fj or fi == fj:
            continue

        # Solve diophantine equation
        # fi * x * fn = fj + y * fn
        # fn * x - fn * y + fi - fj = 0
        # ax + by = c has s solution when gcd(a, b) | c
        c = fj - fi
        if c % g == 0:
            # Because a = -b, the solutions are always of the form
            # x = t, y = t + (fi - fj / fn)
            # we chose t = 0
            n = -c / fn

            # The position of the duplicate
            pos = max(i, j) + abs(n) * fn
            if min_pos is None or pos < min_pos:

                min_pos = pos
                solution = n, fi, fj

n, fi, fj = solution
print "%d = %d + %d * %d" % (fi, fj, n, fn)
