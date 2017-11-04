#!/usr/bin/env python
import binascii

d = bytearray("""Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal""", 'utf8')
key = bytearray("ICE" * 100, 'utf8')
r = bytearray(a ^ b for (a, b) in zip(d, key))

print(binascii.hexlify(r))
