#!/usr/bin/env python3
import copy

def run_prog(prog):
    ip = 0
    acc = 0
    seen = []

    while True:
        if ip >= len(prog):
            return (True, acc)
        if ip in seen:
            return (False, acc)

        seen.append(ip)

        op, imm = prog[ip]
        if op == 'acc':
            acc += imm
        elif op == 'jmp':
            ip += imm - 1

        ip += 1


if __name__ == "__main__":
    prog = []
    with open('input_08') as f:
        for line in f:
            opcode, imm = line.strip().split()
            prog.append((opcode, int(imm)))

    print(run_prog(prog)[1])

    for i, (opcode, imm) in enumerate(prog):
        new_prog = copy.copy(prog)
        if opcode == 'nop':
            new_prog[i] = ('jmp', imm)
        elif opcode == 'jmp':
            new_prog[i] = ('nop', imm)
        else:
            continue

        finished, acc = run_prog(new_prog)
        if finished:
            print(acc)
            break
