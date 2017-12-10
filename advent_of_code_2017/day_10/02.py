N = 256
l = range(0, N)

inputs = map(ord, open('input.txt').read().rstrip())
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

print ''.join(dense_hash)
