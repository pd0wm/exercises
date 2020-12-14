#!/usr/bin/env python3
from collections import defaultdict

def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def get_unset_bit_indices(val):
    return [i for i in range(36) if (~val >> i) & 0x1]

def generate_addrs(addr, bits):
    if len(bits) == 0:
        return [addr]

    b = bits[0]
    return generate_addrs(clear_bit(addr, b), bits[1:]) + generate_addrs(set_bit(addr, b), bits[1:])


for part1 in (True, False):
    mem = defaultdict(int)

    with open('input_14') as f:
        for line in f:
            line = line.strip()

            if line.startswith('mask'):
                mask = line.split(' ')[-1]
                mask_set = int(mask.replace('0', '1').replace('X', '0'), 2)
                mask_vals = int(mask.replace('X', '0'), 2)
            else:
                addr = int(line[4:line.find(']')])
                val = int(line.split(' ')[-1])

                if part1:
                    to_write = mask_vals | (val & ~mask_set)
                else:
                    to_write = val

                if part1:
                    mem[addr] = to_write
                else:
                    addr = addr | (mask_set & mask_vals)
                    floating = get_unset_bit_indices(mask_set)
                    for a in generate_addrs(addr, floating):
                        mem[a] = to_write

    print(sum(mem.values()))
