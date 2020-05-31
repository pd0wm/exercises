#!/usr/bin/env python3

from cryptography.hazmat.primitives import padding


def pad_pkcs7(s, block_size=None, length=None):
    if length is None:
        num_blocks = len(s) // block_size
        length = (num_blocks + 1) * block_size

    n_pad = length - len(s)
    pad_char = bytes([n_pad])
    return s + pad_char * n_pad


if __name__ == "__main__":
    assert(pad_pkcs7(b"YELLOW SUBMARINE", length=20) == b"YELLOW SUBMARINE\x04\x04\x04\x04")
    assert(pad_pkcs7(b"YELLOW SUBMARINE", block_size=20) == b"YELLOW SUBMARINE\x04\x04\x04\x04")

    padder = padding.PKCS7(20 * 8).padder()
    assert(pad_pkcs7(b"YELLOW SUBMARINE", block_size=20) == padder.update(b"YELLOW SUBMARINE") + padder.finalize())
