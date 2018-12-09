#!/usr/bin/env python3
from collections import defaultdict
import networkx as nx
from networkx.algorithms.dag import lexicographical_topological_sort

DG = nx.DiGraph()
for line in open('input.txt'):
    DG.add_edge(line[5], line[36])

topo_sort = "".join(lexicographical_topological_sort(DG))
print(topo_sort)


done = []
time_left = {}
for k in topo_sort:
    time_left[k] = ord(k) - ord('A') + 61

cur_work = []
workers_available = 6
time_spent = 0

while True:
    ready = list()

    for n in topo_sort:
        can_start = True
        in_edges = DG.in_edges(n)
        for k, v in in_edges:
            if k not in done:
                can_start = False
                break

        if can_start and n not in done:
            ready.append(n)

    if len(ready) == 0:
        break

    # Assign tasks to workes
    for w, in ready:
        if w not in cur_work:
            cur_work.append(w)
            workers_available -= 1
        if workers_available == 0:
            break

    # Do the work
    new_work = list()
    for w in cur_work:
        time_left[w] -= 1
        if time_left[w] == 0:
            done.append(w)
            workers_available += 1
        else:
            new_work.append(w)
    cur_work = new_work

    time_spent += 1

print(time_spent)
