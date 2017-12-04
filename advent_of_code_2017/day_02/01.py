f = open("input_01.txt")

checksum = 0
for line in f:
    numbers = list(map(int, line.rstrip().split('\t')))
    checksum += max(numbers) - min(numbers)

print(checksum)
