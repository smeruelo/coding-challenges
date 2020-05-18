# https://exercism.io/my/solutions/0d46e2263b49460dbee50fcf8a0f7d80

# Stone are nodes in a graph. A circular chain is then a Hamiltonian path.
# So this is NP-hard, no good solution -> let's bruteforce it.
# Nodes are tuples (ID, stone)
# IDs are necessary to use sets, since there can be duplicated stones.

from collections import namedtuple

Stone = namedtuple('Stone', 'left right')
Node = namedtuple('Node', 'id stone')

def adjacents(value, nodes):
    return set(filter(lambda n: value in n.stone, nodes))

def reverse(node):
    return Node(node.id, Stone(node.stone.right, node.stone.left))

def can_chain(dominoes):
    def rec(chain, rest):
        if not rest:
            return chain if chain[-1].right == chain[0].left else None
        for n in adjacents(chain[-1].right, rest):
            nxt = n if n.stone.left == chain[-1].right else reverse(n)
            if (result := rec(chain + [nxt.stone], rest - {n})) is not None:
                return result
        return None

    if dominoes == []:
        return []
    stones = map(lambda s: Stone(*s), dominoes)
    nodes = set(map(lambda n: Node(*n), zip(range(len(dominoes)), stones)))
    return rec([nodes.pop().stone], nodes)
