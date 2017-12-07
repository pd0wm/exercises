f = open('input_01.txt')

parents = {}

for line in f:
    p = line.split(' ')[0]

    c = line.split(' -> ')
    if len(c) > 1:
        children = c[1].rstrip().split(', ')

        for child in children:
            parents[child] = p

p = parents.keys()[0]
while True:
    if p not in parents:
        print p
        break
    p = parents[p]
