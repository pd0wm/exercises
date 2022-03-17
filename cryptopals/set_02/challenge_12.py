#!/usr/bin/env python3

import os
import base64
from helpers import blocks, encrypt_ecb, decrypt_ecb

MAGIC_STRING = base64.b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")


def ecb_encryption_oracle(prefix):
    plaintext = prefix + MAGIC_STRING
    return encrypt_ecb(plaintext)


def find_block_size():
    len_empty = len(ecb_encryption_oracle(b""))

    n = 1
    n_1 = None
    len_1 = None

    while True:
        cur_len = len(ecb_encryption_oracle(b"A" * n))
        if n_1 is not None and cur_len != len_1:
            return n - n_1

        if cur_len != len_empty and n_1 is None:
            n_1 = n
            len_1 = cur_len

        n += 1


if __name__ == "__main__":
    block_size = find_block_size()
    assert block_size == 16

    decrypted = b""

    while True:
        pad_length = (block_size - len(decrypted) - 1) % block_size

        prefix = b"A" * pad_length
        compare_length = pad_length + len(decrypted) + 1
        ciphertext = ecb_encryption_oracle(prefix)

        for j in range(256):
            c = ecb_encryption_oracle(prefix + decrypted + bytes([j]))
            if c[:compare_length] == ciphertext[:compare_length]:
                decrypted += bytes([j])
                break
        else:
            # No match found
            break

    print(decrypted)
