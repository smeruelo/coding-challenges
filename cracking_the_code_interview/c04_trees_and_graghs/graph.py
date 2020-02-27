from collections import defaultdict


class Graph():
    def __init__(self, values, edges):
        self._adj = defaultdict(set)
        self._nodes = defaultdict(int)  # Let's asume nodes store int values
        self._load_values(values)
        self._load_edges(edges)

    def _load_values(self, values):
        for nid, val in values:
            self._nodes[nid] = val

    def _load_edges(self, edges):
        pass

    def node_value(self, nid):
        if nid in self._nodes:
            return self._nodes[nid]
        else:
            raise NodeNotFoundException

    def node_neighbors(self, nid):
        if nid in self._nodes:
            return self._adj[nid]
        else:
            raise NodeNotFoundException


class DirectedGraph(Graph):
    def _load_edges(self, edges):
        for nid_src, nid_dst in edges:
            self._adj[nid_src].add(nid_dst)


class UndirectedGraph(Graph):
    def _load_edges(self, edges):
        for nid_1, nid_2 in edges:
            self._adj[nid_1].add(nid_2)
            self._adj[nid_2].add(nid_1)


class NodeNotFoundException(Exception):
    pass
