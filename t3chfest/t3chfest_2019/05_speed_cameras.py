# task 5
# Brute force solution, valid only for small values of N

from itertools import combinations


def adjacency_list(A, B, cuts):
    t = [[] for _ in range(len(A) + 1)]
    for edge, (node_a, node_b) in enumerate(zip(A, B)):
        if edge not in cuts:
            t[node_a].append(node_b)
            t[node_b].append(node_a)
    return t


def furthest(tree, node):
    # DFS traverse a tree to find the furthest node from the one given

    visited = set()

    def dfs(node, length):
        visited.add(node)
        max_distance = length
        max_distance_node = node
        children = set(tree[node]) - visited
        for child in children:
            distance_node, distance = dfs(child, length + 1)
            if distance > max_distance:
                max_distance = distance
                max_distance_node = distance_node
        return(max_distance_node, max_distance)

    return dfs(node, 0)


def longest_path(tree, node):
    # We choose an arbitrary node a in the tree and find the furthest node b from a.
    # Then we find the furthest node c from b. The diameter is the distance between b and c.

    node_b, _ = furthest(tree, node)
    node_c, distance = furthest(tree, node_b)
    return distance


def solution(A, B, num_cameras):
    num_edges = len(A)
    tree = adjacency_list(A, B, [])
    shortest_longest_path = longest_path(tree, 0)

    if num_cameras > 0:
        for combination in combinations(list(range(num_edges)), num_cameras):
            forest = adjacency_list(A, B, combination)
            longest = 0
            for cut in combination:
                longest_a = longest_path(forest, A[cut])
                longest_b = longest_path(forest, B[cut])
                longest = max(longest, longest_a, longest_b)
            shortest_longest_path = min(shortest_longest_path, longest)

    return shortest_longest_path
