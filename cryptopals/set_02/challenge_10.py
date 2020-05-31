#!/usr/bin/env python3

import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b"YELLOW SUBMARINE"
BLOCK_SIZE = 16


def blocks(l, n=BLOCK_SIZE):
    for i in range(0, len(l) // n):
        yield l[i * n: (i + 1) * n]


if __name__ == "__main__":
    with open('10.txt') as f:
        ciphertext = base64.b64decode(f.read())

        backend = default_backend()
        cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=backend)

        iv = b"\x00" * BLOCK_SIZE

        plaintext = ""
        for ciphertext_block in blocks(ciphertext):
            decryptor = cipher.decryptor()
            plaintext_block = decryptor.update(ciphertext_block) + decryptor.finalize()
            plaintext_block = bytes([a ^ b for (a, b) in zip(iv, plaintext_block)])
            plaintext += plaintext_block.decode('utf8')

            iv = ciphertext_block

        print(plaintext)

        iv = b"\x00" * BLOCK_SIZE
        cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()
        plaintext_check = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext_check = plaintext_check.decode('utf8')

        assert(plaintext_check == plaintext)
