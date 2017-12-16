def dance(programs, instructions, history):
    p = programs[:]
    N = len(p)
    for i in instructions:
        if i.startswith('s'):
            n = int(i[1:])
            p = p[-n:] + p[:N - n]
        elif i.startswith('x'):
            i = i[1:].split('/')
            a = int(i[0])
            b = int(i[1])
            p[b], p[a] = p[a], p[b]
        elif i.startswith('p'):
            a = p.index(i[1])
            b = p.index(i[3])
            p[b], p[a] = p[a], p[b]

    s = ''.join(p)
    if s in history:
        return p, True
    else:
        history.append(s)
        return p, False


instructions = open('input.txt').read().rstrip().split(',')
programs = map(chr, range(ord('a'), ord('p') + 1))
history = [''.join(programs)]

programs, _ = dance(programs, instructions, history)
print 'part 1:', history[-1]

done = False
while not done:
    programs, done = dance(programs, instructions, history)

print 'part 2:', history[1000000000 % len(history)]
