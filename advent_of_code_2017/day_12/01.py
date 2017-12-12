programs = {}

for line in open('input.txt'):
    l = line.split(' <-> ')

    i = int(l[0])
    children = map(int, l[1].split(','))

    programs[i] = children[:]
    for c in children:
        if c not in programs:
            programs[c] = [i]
        else:
            if i not in programs[c]:
                programs[c].append(i)

visited = []


def count_connected_programs(i, visited):
    if i in visited:
        return 0

    visited.append(i)
    s = 1
    for c in programs[i]:
        s += count_connected_programs(c, visited)

    return s


print 'part 1:', count_connected_programs(0, visited)


groups = 1
for i in range(max(programs.keys()) + 1):
    if count_connected_programs(i, visited):
        groups += 1

print 'part 2:', groups
