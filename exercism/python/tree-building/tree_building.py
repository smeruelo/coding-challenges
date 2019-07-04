class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    records.sort(key=lambda x: x.record_id)
    n = len(records)
    if n == 0:
        return None
    if records[0].record_id != 0:
        raise ValueError('Tree must start with id 0')
    if records[0].parent_id != 0:
        raise ValueError('Root node cannot have a parent')

    children = [[] for _ in range(n)]
    for r in records[1:]:
        if r.parent_id not in range(n) or r.record_id not in range(n):
            raise ValueError('Tree must be continuous')
        if r.record_id < r.parent_id:
            raise ValueError('Parent id must be lower than child id')
        if r.record_id == r.parent_id:
            raise ValueError('Tree is a cycle')
        children[r.parent_id].append(r.record_id)

    def bfs(current):
        for child in children[current.node_id]:
            node = bfs(Node(child))
            current.children.append(node)
        return current

    return bfs(Node(0))
