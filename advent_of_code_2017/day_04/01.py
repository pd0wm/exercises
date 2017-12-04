from collections import Counter
f = open("input_01.txt")

valid = 0

for line in f:
    words = line.rstrip().split(" ")
    words = Counter(words)
    if max(words.values()) < 2:
        valid += 1

print(valid)
