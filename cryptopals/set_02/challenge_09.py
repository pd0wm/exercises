#!/usr/bin/env python3


def pad_pkcs7(s, block_size=None, length=None):
    if length is None:
        if len(s) % block_size == 0:
            return s  # No padding needed
        num_blocks = len(s) // block_size
        length = (num_blocks + 1) * block_size

    n_pad = length - len(s)
    pad_char = bytes([n_pad])
    return s + pad_char * n_pad


if __name__ == "__main__":
    assert(pad_pkcs7(b"YELLOW SUBMARINE", length=20) == b"YELLOW SUBMARINE\x04\x04\x04\x04")
    assert(pad_pkcs7(b"YELLOW SUBMARINE", block_size=20) == b"YELLOW SUBMARINE\x04\x04\x04\x04")

    # No padding needed
    assert(pad_pkcs7(b"YELLOW SUBMARINE", length=16) == b"YELLOW SUBMARINE")
    assert(pad_pkcs7(b"YELLOW SUBMARINE", block_size=8) == b"YELLOW SUBMARINE")
