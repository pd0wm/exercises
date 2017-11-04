#!/usr/bin/env python3
d = bytes.fromhex("1c0111001f010100061a024b53535009181c")
d2 = bytes.fromhex("686974207468652062756c6c277320657965")

r = bytes([a ^ b for (a, b) in zip(d, d2)])
print(r.hex())
