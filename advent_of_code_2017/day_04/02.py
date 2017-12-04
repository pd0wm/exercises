from collections import Counter
from itertools import permutations

f = open("input_01.txt")

valid = 0

for line in f:
    words = line.rstrip().split(" ")

    no_duplicates = True
    for word in words:
        other_words = words[:]
        other_words.remove(word)

        other_words = set(other_words)
        perms = set([''.join(p) for p in permutations(word)])

        intersect = perms & other_words
        if len(intersect) > 0:
            no_duplicates = False

    if no_duplicates:
        valid += 1

print(valid)
