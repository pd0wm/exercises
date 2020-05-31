#!/usr/bin/env python3

import base64
from collections import Counter


def chunks(l, n=2):
    for i in range(0, len(l) // n):
        yield l[i * n: (i + 1) * n]


if __name__ == "__main__":
    with open('8.txt') as f:

        # We chop up the ciphertexts into blocks of two bytes, then use
        # Counter to find the line with the most duplicate blocks
        num_duplicates = []
        for i, line in enumerate(f):
            ciphertext = base64.b64decode(line)
            two_bytes = list(chunks(ciphertext))
            counter = Counter(two_bytes)

            num_duplicates.append((max(counter.values()), i))

        max_i = sorted(num_duplicates, reverse=True)[0][1]
        print(max_i)
