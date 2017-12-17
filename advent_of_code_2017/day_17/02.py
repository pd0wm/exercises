step = 349

cur_pos = 0
for i in range(1, 50000000 + 1):
    pos = (cur_pos + step) % i
    if cur_pos == 1:
        print i - 1
    cur_pos = pos + 1
