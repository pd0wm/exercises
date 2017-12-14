scanners = []
for line in open('input.txt'):
    scanners.append(map(int, line.rstrip().split(': ')))

print sum([depth * r if depth % (2 * r - 2) == 0 else 0 for (depth, r) in scanners])

delay = 0
while True:
    found = True
    for depth, r in scanners:
        if (delay + depth) % (2 * r - 2) == 0:
            found = False
            break

    if found:
        print delay
        break

    delay += 1
