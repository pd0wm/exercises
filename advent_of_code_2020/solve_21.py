#!/usr/bin/env python3
import time

from collections import defaultdict

inp = defaultdict(list)

all_ingredients = []

with open('input_21') as f:
    for line in f:
        line = line.strip()

        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        all_ingredients += ingredients

        allergens = allergens[:-1].split(', ')

        for a in allergens:
            inp[a].append(set(ingredients))


possible = {}

for allergen, ingredients in inp.items():
    r = ingredients[0]
    for i in ingredients:
        r &= i

    possible[allergen] = r

while max([len(x) for x in possible.values()]) > 1:
    for k, v in possible.items():
        if len(v) == 1:
            for a in possible:
                if a != k:
                    possible[a] -= v

matches = {}
for k, v in possible.items():
    matches[k] = list(v)[0]

# Part 1
unsafe_ingredients = list(matches.values())
safe = [i for i in all_ingredients if i not in unsafe_ingredients]
print(len(safe))

# Part 2
print(",".join([v for (k, v) in sorted(matches.items())]))
