from collections import defaultdict

instructions = open('input.txt').read().split('\n')

d = defaultdict(int)
d['pc'] = 0
while True:
    line = instructions[d['pc']]
    if line.startswith('snd'):
        ins = line.replace('snd', 'snd = ')
        d['pc'] += 1
    if line.startswith('rcv'):
        l = line.split()
        if 'snd' in d:
            print d['snd']
            break
            ins = l[1] + ' = snd'
        else:
            ins = ''
        d['pc'] += 1
    elif line.startswith('set'):
        l = line.split()
        ins = l[1] + ' = ' + l[2]
        d['pc'] += 1
    elif line.startswith('mul'):
        l = line.split()
        ins = l[1] + ' *= ' + l[2]
        d['pc'] += 1
    elif line.startswith('add'):
        l = line.split()
        ins = l[1] + ' += ' + l[2]
        d['pc'] += 1
    elif line.startswith('mod'):
        l = line.split()
        ins = l[1] + ' %= ' + l[2]
        d['pc'] += 1
    elif line.startswith('jgz'):
        l = line.split()
        ins = 'pc += ' + l[2] + ' if ' + l[1] + ' > 0 else 1'

    exec(ins, {}, d)
