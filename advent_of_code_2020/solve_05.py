#!/usr/bin/env python3
def decode(s):
    s = s.replace('F', '0')
    s = s.replace('B', '1')
    s = s.replace('L', '0')
    s = s.replace('R', '1')
    return int(s, 2)


with open('input_05') as f:
    ids = [decode(l) for l in f]

print(max(ids))

all_ids = set(range(min(ids), max(ids)))
print(all_ids - set(ids))
