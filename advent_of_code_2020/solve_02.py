#!/usr/bin/env python3
from collections import Counter


good_1 = 0
good_2 = 0
with open('input_02') as f:
    for line in f:
        x = line.strip().split(' ')

        l, u = [int(a) for a in x[0].split('-')]
        c = x[1][0]
        passwd = x[2]

        cnt = Counter(passwd)
        if l <= cnt[c] <= u:
            good_1 += 1

        a = passwd[l - 1] == c
        b = passwd[u - 1] == c

        if a != b:
            good_2 += 1

print(good_1)
print(good_2)
