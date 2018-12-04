#!/usr/bin/env python2

f = open('input.txt')
import datetime
import numpy as np
from collections import defaultdict


# Types of events
WAKEUP = 1
SLEEPS = 2
NEW_GUARD = 3


# Build list of events that can be sorted later
events = []
for line in f:
    line = line.rstrip()

    # Time parsing
    time = line[1:].split(']')[0].replace('-', ' ').replace(':', ' ')
    time = time.split(' ')
    time = map(int, time)
    dtime = datetime.datetime(*time)

    # Create correct event
    if 'wakes' in line:
        event = (WAKEUP, 0)
    elif 'falls' in line:
        event = (SLEEPS, 0)
    elif 'Guard' in line:
        guard = int(line[line.find('#'):][1:].split(' ')[0])
        event = (NEW_GUARD, guard)
    events.append((dtime, event))


# Sort events by date
events.sort(key=lambda x: x[0])


# Create dict with lists for each guard indicating how many times they were asleep at that minute
cur_guard = -1
sleep_start = -1
guards = defaultdict(lambda : np.zeros(60))
for time, (event, guard_id) in events:
    if event == NEW_GUARD:
        cur_guard = guard_id
    elif event == SLEEPS:
        sleep_start = time.minute
    elif event == WAKEUP:
        sleep_end = time.minute
        guards[cur_guard][sleep_start:sleep_end] += 1


# Turn dict into useful numpy arrays
guard_ids = []
minutes = []
for g, m in guards.items():
    guard_ids.append(g)
    minutes.append(m)
minutes = np.asarray(minutes)

# Question 1
totals = np.sum(minutes, axis=1)
most_asleep_guard = np.argmax(totals)
print guard_ids[most_asleep_guard] * np.argmax(minutes[most_asleep_guard])


# Question 2
m = np.unravel_index(np.argmax(minutes, axis=None), minutes.shape)
print guard_ids[m[0]] * m[1]
