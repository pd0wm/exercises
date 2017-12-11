import numpy as np

commands = open('input.txt').read().rstrip().split(',')

DIRS = {
    'n': np.array([0, 1, -1]),
    'ne': np.array([1, 0, -1]),
    'se': np.array([1, -1, 0]),
    's': np.array([0, -1, 1]),
    'sw': np.array([-1, 0, 1]),
    'nw': np.array([-1, 1, 0]),
}

pos = np.array([0, 0, 0])
max_dist = 0

for c in commands:
    pos += DIRS[c]
    max_dist = max(max_dist, np.max(pos))

print 'part 1:', np.max(pos)
print 'part 2:', max_dist
