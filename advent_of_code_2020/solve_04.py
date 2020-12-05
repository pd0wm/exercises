#!/usr/bin/env python3
needs = {'byr', 'iyr', 'eyr', 'hgt', 'hcl',
         'ecl', 'pid'}

passports = []

with open('input_04') as f:
    d = {}
    for line in f:
        line = line.strip()

        if not line:
            passports.append(d)
            d = {}
            continue

        kv = [x.split(':') for x in line.split(' ')]
        for k, v in kv:
            d[k] = v
passports.append(d)

valid1 = 0
valid2 = 0
for p in passports:
    missing = needs - set(p.keys())
    if len(missing) == 0:
        valid1 += 1
    else:
        continue

    byr = int(p['byr'])
    if not (1920 <= byr <= 2002):
        continue
    iyr = int(p['iyr'])
    if not (2010 <= iyr <= 2020):
        continue
    eyr = int(p['eyr'])
    if not (2020 <= eyr <= 2030):
        continue

    hgt = int(p['hgt'][:-2])
    hgt_unit = p['hgt'][-2:]
    if hgt_unit == 'cm':
        if not (150 <= hgt <= 193):
            continue
    else:
        if not (59 <= hgt <= 76):
            continue

    hcl = p['hcl']
    if not hcl[0] == '#':
        continue
    if not len(hcl) == 7:
        continue

    ok = ['amb', 'blu', 'brn', 'gry', 'grn',
          'hzl', 'oth']
    if p['ecl'] not in ok:
        continue

    pid = p['pid']
    if len(pid) != 9:
        continue
    valid2 += 1


print(valid1)
print(valid2)
