#!/usr/bin/env python3

from collections import defaultdict, deque

circle = deque()
circle.append(0)

scores = defaultdict(int)

num_players = 403
marbles = 71920 * 100

for i in range(1, marbles + 1):
    if i % 23 == 0:
        circle.rotate(7)
        scores[i % num_players] += i
        scores[i % num_players] += circle.pop()
        circle.rotate(-1)

    else:
        circle.rotate(-1)
        circle.append(i)

print(max(scores.values()))
