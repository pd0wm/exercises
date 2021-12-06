#!/usr/bin/env python3
from collections import defaultdict
from typing import Counter

def step(fish):
    new_fish = defaultdict(int)
    for age, count in fish.items():
        if age == 0:
            new_fish[6] += count
            new_fish[8] += count
        else:
            new_fish[age - 1] += count
    return new_fish

if __name__ == "__main__":
    inp = [int(n) for n in open("input_06").read().split(',')]
    fish = defaultdict(int, Counter(inp))

    for _ in range(80):
        fish = step(fish)
    print(sum(fish.values()))

    for _ in range(256 - 80):
        fish = step(fish)
    print(sum(fish.values()))
