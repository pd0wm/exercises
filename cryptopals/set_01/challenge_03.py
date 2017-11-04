#!/usr/bin/env python3
d = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

solutions = []
for c in range(256):
    solutions.append(bytes([a ^ c for a in d]))

for s in sorted(solutions, key=lambda t: sum([t.count(ord(c)) for c in ('a', 'e', 'u', 'o', 'i')])):
    print(s)
