#!/usr/bin/env python3

ranges = {}
tickets = []

with open('input_16') as f:
    for line in f:
        line = line.strip()

        if not line:
            break

        line = line.split(': ')
        name = line[0]
        rng = [(int(x.split('-')[0]), int(x.split('-')[1])) for x in line[1].split(' or ')]
        ranges[name] = set(range(rng[0][0], rng[0][1]+1)) | set(range(rng[1][0], rng[1][1]+1))

    next(f)
    # Your ticket
    your_ticket = [int(x) for x in next(f).strip().split(',')]

    next(f)
    next(f)
    # Nearby tickets
    for line in f:
        tickets.append([int(x) for x in line.strip().split(',')])

valid_tickets = []

solution_01 = 0
for t in tickets:
    valid = True
    for v in t:
        found = False

        for r in ranges.values():
            if v in r:
                found = True
                break

        if not found:
            valid = False
            solution_01 += v

    if valid:
        valid_tickets.append(t)
print(solution_01)

N = len(your_ticket)

# Build a set of values seen for each position in the ticket
used = [set([]) for _ in range(N)]
for t in valid_tickets:
    for i, v in enumerate(t):
        used[i] |= set([v])

# Figure out for which ranges we can't find any contradictions in the the ticket values
rng = list(ranges.values())
valid = []
for i in range(N):
    valid.append(set([j for j in range(N) if len(used[j] - rng[i]) == 0]))

# If a certain index has only one possible value, this value can't be used in other places
# Keep removing single values until everything has only one possiblity
while max([len(x) for x in valid]) > 1:
    for i, v in enumerate(valid):
        if len(v) == 1:
            for j in range(N):
                if j == i:
                    continue
                valid[j] = valid[j] - set(v)


# Compute solution
solution_02 = 1
for i in range(6):
    solution_02 *= your_ticket[list(valid[i])[0]]
print(solution_02)
