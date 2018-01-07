from collections import defaultdict, deque

class Program(object):
    def __init__(self, p):
        self.instructions = open('input.txt').read().split('\n')
        self.d = defaultdict(int)
        self.d['p'] = p
        self.wait_recv = False
        self.recv_reg = None
        self.output = deque()
        self.done = False
        self.snd_count = 0

    def receive_value(self, val):
        self.d[self.recv_reg] = val
        self.d['pc'] += 1
        self.wait_recv = False

    def run(self):
        while True:
            line = self.instructions[self.d['pc']]
            if line.startswith('snd'):
                ins = line.replace('snd', 'snd = ')
                self.d['pc'] += 1
            if line.startswith('rcv'):
                l = line.split()
                self.wait_recv = True
                self.recv_reg = l[1]
                return
            elif line.startswith('set'):
                l = line.split()
                ins = l[1] + ' = ' + l[2]
                self.d['pc'] += 1
            elif line.startswith('mul'):
                l = line.split()
                ins = l[1] + ' *= ' + l[2]
                self.d['pc'] += 1
            elif line.startswith('add'):
                l = line.split()
                ins = l[1] + ' += ' + l[2]
                self.d['pc'] += 1
            elif line.startswith('mod'):
                l = line.split()
                ins = l[1] + ' %= ' + l[2]
                self.d['pc'] += 1
            elif line.startswith('jgz'):
                l = line.split()
                ins = 'pc += ' + l[2] + ' if ' + l[1] + ' > 0 else 1'

            exec(ins, {}, self.d)
            if 'snd' in self.d:
                self.output.append(self.d['snd'])
                self.snd_count += 1
                del self.d['snd']

            if self.d['pc'] < 0 or self.d['pc'] > len(self.instructions):
                self.done = True
                return

p1 = Program(0)
p2 = Program(1)
p1.run()
p2.run()

while True:
    while p1.output and p2.wait_recv and not p2.done:
        p2.receive_value(p1.output.popleft())
        p2.run()

    while p2.output and p1.wait_recv and not p1.done:
        p1.receive_value(p2.output.popleft())
        p1.run()

    if (p1.wait_recv and not p2.output) and (p2.wait_recv and not p1.output):
        print "deadlock"
        break

    if p1.done and p2.done:
        print "done"
        break

print p2.snd_count
