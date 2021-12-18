#!/usr/bin/env python3
import numpy as np
import networkx as nx


def grid_to_graph(tile):
    DG = nx.DiGraph()
    for i in range(0, tile.shape[0]):
        for j in range(0, tile.shape[1]):
            if i - 1 >= 0: DG.add_edge((i, j), (i - 1, j), weight=tile[i - 1, j])
            if i + 1 < tile.shape[0]: DG.add_edge((i, j), (i + 1, j), weight=tile[i + 1, j])
            if j - 1 >= 0: DG.add_edge((i, j), (i, j - 1), weight=tile[i, j - 1])
            if j + 1 < tile.shape[1]: DG.add_edge((i, j), (i, j + 1), weight=tile[i, j + 1])
    return DG

def len_path(tile):
    N = tile.shape[0] - 1
    DG = grid_to_graph(tile)
    path = nx.shortest_path(DG, source=(0, 0), target=(N, N), weight='weight')
    return nx.classes.path_weight(DG, path, weight='weight')

if __name__ == "__main__":
    tile = []
    for line in open('input_15'):
        tile.append(list(map(int, line.strip())))
    tile = np.asarray(tile)

    full_map = []
    for i in range(5):
        full_map.append(np.hstack([tile + np.ones_like(tile) * (i + j) for j in range(5)]))
    full_map = np.vstack(full_map)
    full_map = ((full_map  - 1) % 9) + 1

    print(len_path(tile))
    print(len_path(full_map))