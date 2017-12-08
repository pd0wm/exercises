from collections import defaultdict


r = defaultdict(lambda: 0)

max_val = 0

for line in open('input.txt'):
    l = line.rstrip()
    l = l.replace('inc', '+=')
    l = l.replace('dec', '-=')
    l += ' else 0'

    l = l.split(' ')
    l = 'r[\'%s\'] ' % l[0] + ' '.join(l[1:4]) + ' r[\'%s\'] ' % l[4] + ' '.join(l[5:])
    exec(l)
    max_val = max(max_val, max(r.values()))


print r
print 'part 1', max(r.values())
print 'part 2', max_val
