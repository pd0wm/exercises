#!/usr/bin/env python3
import os
import urllib.parse

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

KEY = os.urandom(16)

def blocks(l, n=16):
    for i in range(0, len(l) // n):
        yield l[i * n: (i + 1) * n]

def encrypt_ecb(plaintext):
    if not isinstance(plaintext, bytes):
        plaintext = plaintext.encode()

    padder = padding.PKCS7(16 * 8).padder()
    plaintext = padder.update(plaintext) + padder.finalize()

    backend = default_backend()
    cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    return encryptor.update(plaintext) + encryptor.finalize()

def decrypt_ecb(cipertext):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=backend)

    decryptor = cipher.decryptor()
    plaintext = decryptor.update(cipertext) + decryptor.finalize()

    unpadder = padding.PKCS7(16 * 8).unpadder()
    plaintext = unpadder.update(plaintext) + unpadder.finalize()
    plaintext = plaintext.decode()
    return plaintext


def profile_for(email):
    # This is what I wrote at first, but actually makes it unsolvable
    # due to escaping non printable chars.
    # profile = {'email': email, 'uid': 10, 'role': 'user'}
    # profile_qs = urllib.parse.urlencode(profile)

    # Use this naive implementation instead
    email = email.replace('=', '').replace('&', '')
    profile_qs = f"email={email}&uid=10&role=user"

    return encrypt_ecb(profile_qs)

def get_role(profile):
    try:
        profile = decrypt_ecb(profile)
        p = urllib.parse.parse_qs(profile, strict_parsing=True)
        return p['role'][0]
    except Exception:
        return None


if __name__ == "__main__":
    assert get_role(profile_for("foo@bar.com")) == 'user'
    assert get_role(profile_for("foo@bar.com&role=admin")) == 'user'

    block_size = 16

    # Build crafted payload to obtain block 1
    # Block 0: email=<pad1>
    # Block 1: admin + PKCS7 padding
    # Block 2: &uid=10&role=use
    # Block 3: r + PCKS7 padding

    pad1 = "A" * (block_size - len("email="))
    padder = padding.PKCS7(16 * 8).padder()
    admin = padder.update(b"admin") + padder.finalize()
    _, admin_block, _, _ = blocks(profile_for(pad1 + admin.decode()))

    # Build new payload and replace block 2 by previously obtained block 1
    # Block 0: email=<pad1>
    # Block 1: <pad2>&uid=10&role=
    # Block 2: user + PCKS7 padding

    pad2 = "A" * (block_size - len("&uid=10&role="))
    b0, b1, _ = blocks(profile_for(pad1 + pad2))
    payload = b0 + b1+ admin_block

    assert get_role(payload) == 'admin'


