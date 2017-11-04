#!/usr/bin/env python3
import base64
from challenge_04 import english_score

def hamming(s1, s2):
    return sum([bin(a).count("1") for a in bytearray(a ^ b for a, b in zip(s1, s2))])

f = open('6.txt', 'rb')
d = base64.decodebytes(f.read())

# Find optimal keysize
smallest = 100
smallest_keysize = -1
for keysize in range(2, 40):
    r = 0
    for i in range(30):
        r += hamming(d[i*keysize:(i+1)*keysize], d[(i+1)*keysize:(i+2)*keysize]) / keysize

    print(keysize, r)
    if r < smallest:
        smallest = r
        smallest_keysize = keysize
print()
print(smallest_keysize)

keysize = smallest_keysize

# Find key
key = ""
for i in range(keysize):
    block = d[i::keysize]

    solutions = []
    for c in range(32, 128):
        solutions.append((c, bytes([a ^ c for a in block])))

    solutions = sorted(solutions, key=lambda t: english_score(t[1]))
    key += chr(solutions[-1][0])

# Docode input with key
r = bytearray(a ^ b for (a, b) in zip(d, bytearray(key * 1000, 'utf8')))

print(r.decode('utf8'))
print(f"The key is -- {key}")
