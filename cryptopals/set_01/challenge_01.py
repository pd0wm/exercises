#!/usr/bin/env python3
import base64

d = bytes.fromhex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

print(d)
print(base64.encodebytes(d))
