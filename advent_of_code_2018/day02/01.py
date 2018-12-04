#!/usr/bin/env python2
from collections import Counter

twos = 0
triples = 0
for line in open('input.txt'):
    line = line.rstrip()
    c = Counter(line).values()
    if c.count(2): twos += 1
    if c.count(3): triples += 1

print twos * triples

for line1 in open('input.txt'):
    for line2 in open('input.txt'):
        d = sum([a != b for a, b in zip(line1, line2)])
        if d == 1:
            print "".join([a for a, b in zip(line1, line2) if a == b])
