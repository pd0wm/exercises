s = "{{},{}}"

s = open('input.txt').read().rstrip()

score = 0
nest = 0
garbage = False
skip = False

garbage_count = 0

for c in s:
    if skip:
        skip = False
        continue

    if c == '!':
        skip = True
        continue

    if c == '>':
        garbage = False

    if garbage:
        garbage_count += 1
        continue

    if c == '<':
        garbage = True
    if c == '{':
        nest += 1
        score += nest

    if c == '}':
        nest -= 1

print 'part 1:', score
print 'part 2:', garbage_count
