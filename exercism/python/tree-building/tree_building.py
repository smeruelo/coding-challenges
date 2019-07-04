class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    n = len(records)
    if n == 0:
        return None
    children = [[] for _ in range(n)]
    parent = [None for _ in range(n)]
    for r in records:
        if r.parent_id not in range(n) or r.record_id not in range(n):
            raise ValueError('Tree must be continuous')
        if r.record_id < r.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if r.record_id == r.parent_id and r.record_id != 0:
            raise ValueError('Tree is a cycle')
        if r.record_id == 0 and r.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
        parent[r.record_id] = r.parent_id
        if r.record_id != 0:
            children[r.parent_id].append(r.record_id)
    if parent[0] is None:
        raise ValueError('Tree must start with id 0')

    def bfs():
        def rec(current):
            for child in sorted(children[current.node_id]):
                node = rec(Node(child))
                current.children.append(node)
            return current
        return rec(Node(0))

    return bfs()
