#!/usr/bin/env python3

import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

KEY = b"YELLOW SUBMARINE"

if __name__ == "__main__":
    with open('7.txt') as f:
        ciphertext = base64.b64decode(f.read())

        backend = default_backend()
        cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=backend)
        decryptor = cipher.decryptor()

        msg = decryptor.update(ciphertext) + decryptor.finalize()
        msg_str = msg.decode('utf8')
        print(msg_str)
