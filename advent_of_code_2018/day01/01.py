#!/usr/bin/env python2

s = 0
freqs = []
for line in open('input.txt'):
    line = line.rstrip()
    if len(line):
        s += int(line)
        freqs.append(s)
print s


total = s
done = False

more_freqs = {}
first = None

cur_freq = 0
while first is None:
    for f in freqs:
        n = f + cur_freq
        if n in more_freqs:
            first = n
            break
        else:
            more_freqs[n] = True

    cur_freq += total



print first
