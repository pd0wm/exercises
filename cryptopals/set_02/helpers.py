import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


BLOCK_SIZE = 16
KEY = os.urandom(BLOCK_SIZE)

def blocks(l, n=BLOCK_SIZE):
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