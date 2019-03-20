# task 5


def adjacency_list(A, B):
    t = [[] for _ in range(len(A) + 1)]
    for node_a, node_b in zip(A, B):
        t[node_a].append(node_b)
        t[node_b].append(node_a)
    return t


def solution(A, B, num_cameras):
    # Algorithm explained here: https://cs.stackexchange.com/a/93282

    def dfs(node, parent, limit):
        # Returns (_, cuts), where cuts is the number of cameras needed to grant
        # maximum length of an uncovered path = limit
        s = 0
        cuts = c = 0
        for adj in tree[node]:
            if adj != parent:
                r, c = dfs(adj, node, limit)
                r += 1
                cuts += c
                if r + s > limit:
                    s = min(s, r)
                    cuts += 1
                else:
                    s = max(s, r)
        return s, cuts

    # Binary search over the results of dfs with different limits.
    # Algorithm in Laaksonen (page 33, finding the smallest solution)
    tree = adjacency_list(A, B)
    x = -1
    jump = len(A) + 1
    while jump >= 1:
        _, cuts = dfs(0, None, x + jump)
        while not cuts <= num_cameras:
            x += jump
            _, cuts = dfs(0, None, x + jump)
        jump //= 2
    return x + 1
