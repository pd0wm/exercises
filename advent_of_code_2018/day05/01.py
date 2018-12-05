#!/usr/bin/env python2

def react(s_in):
    s = s_in
    while True:
        s_new = ""
        i = 0

        while i < len(s) - 1:
            a = s[i]
            b = s[i + 1]

            # Check if pair
            if abs(ord(a) - ord(b)) != ord('a') - ord('A'):
                s_new += a
                i += 1

            else:
                i += 2

        # Make sure the last letter gets added
        if i == len(s) - 1:
            s_new += s[-1]

        if s_new == s:
            break

        s = s_new
    return s


s = open('input.txt').read().rstrip()
shortest = len(react(s))
shortest_letter = ''
print shortest
print


for i in range(26):
    letter = chr(ord('a') + i)
    s_new = s.replace(letter, '').replace(letter.upper(), '')
    l = len(react(s_new))
    print letter, l

    if l < shortest:
        shortest = l
        shortest_letter = letter

print
print shortest_letter, shortest
