import numpy as np
from scipy.ndimage.measurements import label


def knot_hash(s):
    N = 256
    l = range(0, N)

    inputs = map(ord, s)
    inputs += [17, 31, 73, 47, 23]

    skip_size = 0
    cur_pos = 0

    for _ in range(64):
        for i in inputs:
            l_new = l[:]

            # Reversing
            for x in range(i):
                l_new[(cur_pos + x) % N] = l[(cur_pos + i - x - 1) % N]

            cur_pos = (cur_pos + i + skip_size) % N
            skip_size += 1
            l = l_new

    dense_hash = []
    for i in range(16):
        r = l[i * 16]
        for j in range(1, 16):
            r ^= l[i * 16 + j]

        dense_hash.append("{:02x}".format(r))

    return ''.join(dense_hash)


puzzle_input = "stpzcrnm"

total = []
for i in range(0, 128):
    s = puzzle_input + '-' + str(i)

    int_hash = int(knot_hash(s), 16)
    bin_hash = "{0:0128b}".format(int_hash)
    list_hash = map(int, bin_hash)

    total.append(list_hash)
total = np.array(total)

_, num_groups = label(total)
print 'part 1:', total.sum()
print 'part 2:', num_groups
