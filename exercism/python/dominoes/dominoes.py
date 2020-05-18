# https://exercism.io/my/solutions/0d46e2263b49460dbee50fcf8a0f7d80

# Stone are nodes in a graph. A circular chain is then a Hamiltonian path.
# So this is NP-hard, no good solution -> let's bruteforce it.
# Nodes are tuples (ID, stone)
# IDs are necessary to use sets, since there can be duplicated stones.

def adjacents(value, nodes):
    return set(filter(lambda n: value in n[1], nodes))

def reverse(node):
    return (node[0], (node[1][1], node[1][0]))

def can_chain(dominoes):
    def rec(chain, rest):
        if not rest:
            return chain if chain[-1][1] == chain[0][0] else None
        for n in adjacents(chain[-1][1], rest):
            nxt = n if n[1][0] == chain[-1][1] else reverse(n)
            if (result := rec(chain + [nxt[1]], rest - {n})) is not None:
                return result
        return None

    if dominoes == []:
        return []
    nodes = set(zip(range(len(dominoes)), dominoes))
    return rec([nodes.pop()[1]], nodes)
