import re
from collections import Counter
f = open('input_01.txt')

parents = {}
weights = {}


# Add all weights and parents to dict
for line in f:
    p = line.split(' ')[0]
    w = int(re.findall('\((\d+)\)', line)[0])

    weights[p] = w

    c = line.split(' -> ')
    if len(c) > 1:
        children = c[1].rstrip().split(', ')

        for child in children:
            parents[child] = p

# Find top
top = None
p = parents.keys()[0]
while True:
    if p not in parents:
        top = p
        break
    p = parents[p]


# Find stack with wrong weight which is as high as possible (lowest weight)
wrong_weight = 999999
wrong_name = None
diff = None


def get_weight(p):
    # Get names and total weights for all children
    child_weights = []
    child_names = []
    for program, parent in parents.items():
        if p == parent:
            child_weights.append(get_weight(program))
            child_names.append(program)

    # Check if the child weights differ
    if len(set(child_weights)) > 1:
        child_weights_counts = Counter(child_weights)
        k = child_weights_counts.keys()

        # Calculate difference in weight
        global diff
        diff = k[1] - k[0]

        # Update global lowest wrong weight
        global wrong_weight, wrong_name
        w = k[0]
        name = child_names[child_weights.index(w)]
        if w < wrong_weight:
            wrong_weight = w
            wrong_name = name

    return weights[p] + sum(child_weights)


get_weight(top)
print weights[wrong_name] + diff
