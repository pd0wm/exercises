step = 349

buf = [0]
cur_pos = 0
for i in range(1, 2018):
    pos = (cur_pos + step) % i
    buf = buf[:pos + 1] + [i] + buf[pos + 1:]
    cur_pos = pos + 1

i = buf.index(2017)
print buf[i + 1]
