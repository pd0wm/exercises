N = 256
l = range(0, N)

inputs = map(int, open('input.txt').read().rstrip().split(','))

skip_size = 0
cur_pos = 0

for i in inputs:
    l_new = l[:]

    # Reversing
    for x in range(i):
        l_new[(cur_pos + x) % N] = l[(cur_pos + i - x - 1) % N]

    cur_pos = (cur_pos + i + skip_size) % N
    skip_size += 1
    l = l_new

print l[0] * l[1], l
