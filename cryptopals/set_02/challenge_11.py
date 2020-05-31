#!/usr/bin/env python3

import os
import random
from collections import Counter

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def chunks(l, n=2):
    for i in range(0, len(l) // n):
        yield l[i * n: (i + 1) * n]


def encryption_oracle(plaintext):
    iv = os.urandom(16)
    key = os.urandom(16)

    m = random.choice(["ecb", "cbc"])

    mode = {
        "ecb": modes.ECB(),
        "cbc": modes.CBC(iv),
    }

    prefix_len = random.randrange(5, 11)
    suffix_len = random.randrange(5, 11)

    plaintext = os.urandom(prefix_len) + plaintext + os.urandom(suffix_len)

    padder = padding.PKCS7(16 * 8).padder()
    plaintext = padder.update(plaintext) + padder.finalize()

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), mode[m], backend=backend)
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    return ciphertext, m


def detect_aes_mode(ciphertext):
    c = list(chunks(ciphertext))
    counter = Counter(c)
    if max(counter.values()) > 2:
        return "ecb"
    else:
        return "cbc"


if __name__ == "__main__":
    for _ in range(1000):
        plaintext = b"A" * 64
        ciphertext, mode = encryption_oracle(plaintext)
        assert mode == detect_aes_mode(ciphertext)
