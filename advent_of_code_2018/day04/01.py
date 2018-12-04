#!/usr/bin/env python2

import numpy as np
from datetime import datetime
from collections import defaultdict

# Load file and sort
f = sorted(open('input.txt').readlines())

guards = defaultdict(lambda : np.zeros(60))
for line in f:
    line = line.rstrip()
    dtime = datetime.strptime(line[1:].split(']')[0], '%Y-%m-%d %H:%M')

    if 'Guard' in line:
        cur_guard = int(line[line.find('#'):][1:].split(' ')[0])
    elif 'falls' in line:
        sleep_start = dtime.minute
    elif 'wakes' in line:
        sleep_end = dtime.minute
        guards[cur_guard][sleep_start:sleep_end] += 1

# Turn dict into useful numpy arrays
guard_ids, minutes = zip(*guards.iteritems())
minutes = np.asarray(minutes)

# Question 1
totals = np.sum(minutes, axis=1)
most_asleep_guard = np.argmax(totals)
print guard_ids[most_asleep_guard] * np.argmax(minutes[most_asleep_guard])

# Question 2
m = np.unravel_index(np.argmax(minutes, axis=None), minutes.shape)
print guard_ids[m[0]] * m[1]
