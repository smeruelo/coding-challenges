# https://exercism.io/my/solutions/f9462d780b9d496f81bd0062df5c28cc

# Variant 1:
#   Iterative.
#   Constraints are checked when building the tree.


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
    children = [[] for _ in range(n)]
    tree = [None] * n

    try:
        for r in records:
            children[r.parent_id].append(r.record_id)
        for i in range(n - 1, -1, -1):
            tree[i] = Node(i)
            for c in children[i]:
                if c <= i and i != 0:
                    raise ValueError("Tree is a cycle, or parent id is higher than child's.")
                if c != 0:
                    tree[i].children.append(tree[c])
    except IndexError:
        raise ValueError('Tree must be continuous and start with id 0')

    return tree[0] if tree else None
