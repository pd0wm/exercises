#!/usr/bin/env python3

def magic(loop, subject=7):
    # subject^loop mod 20201227
    return pow(subject, loop, 20201227)


def find_loop_size(public):
    loop = 1
    while True:
        if public == magic(loop):
            return loop
        loop += 1

if __name__ == "__main__":
    # Sample
    card_public = 5764801
    door_public = 17807724

    # Input
    card_public = 1526110
    door_public = 20175123

    card_loop = find_loop_size(card_public)
    door_loop = find_loop_size(door_public)

    encryption_key = magic(door_loop, card_public)
    assert(encryption_key == magic(card_loop, door_public))

    print(encryption_key)
