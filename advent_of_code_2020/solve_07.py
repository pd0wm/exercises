#!/usr/bin/env python3
import networkx as nx
G = nx.DiGraph()

with open('input_07') as f:
    for line in f:
        c, x = line.strip().replace(' bags', '').replace(' bag', '').replace('.', '').split(' contain ')
        to = x.split(', ')
        
        for t in to:
            if t == 'no other':
                continue
            G.add_edge(t[2:], c, weight=int(t[:2]))

print(len(nx.algorithms.descendants(G, 'shiny gold')))

def count_bags(node):
    return 1 + sum([G.edges[to, node]['weight'] * count_bags(to) for (to, _) in G.in_edges(node)])
print(count_bags('shiny gold') - 1)


