from itertools import permutations
f = open("input_01.txt")

checksum = 0
for line in f:
    numbers = list(map(int, line.rstrip().split('\t')))
    pairs = permutations(numbers, 2)

    for (a, b) in pairs:
        if a % b == 0:
            checksum += a / b
            break

print(checksum)
