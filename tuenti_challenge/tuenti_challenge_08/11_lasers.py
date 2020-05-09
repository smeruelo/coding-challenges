#!/usr/bin/python3

import networkx as nx

def lasers(rows, cols, diamonds):
    g = nx.Graph()
    g.add_nodes_from(range(rows + cols))
    g.add_edges_from(map(lambda x: [x[0], x[1] + rows], diamonds))
    return (rows + cols) - len(nx.max_weight_matching(g))


if __name__ == '__main__':
    for i in range(int(input())):
        rows, cols, d = map(int, input().split())
        diamonds = [list(map(int, input().split())) for _ in range(d)]
        print('Case #{}: {}'.format(i + 1, lasers(rows, cols, diamonds)))
