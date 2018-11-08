#!/usr/bin/python3
# https://www.codechef.com/NOV18B/problems/PRITREE

from math import ceil, sqrt


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, ceil(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def score(tree):
    values, edges = tree
    prime_subtrees = 0

    adj = [set() for _ in range(len(edges) + 2)]
    for edge in edges:
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])

    def sum_tree(root):
        visited = [False] * len(values)
        sum_values = 0

        def dfs(node):
            nonlocal sum_values
            if visited[node]:
                return
            sum_values += values[node]
            visited[node] = True
            for child in adj[node]:
                dfs(child)

        dfs(root)
        return sum_values

    for edge in edges:
        adj[edge[0]].remove(edge[1])
        adj[edge[1]].remove(edge[0])
        prime_subtrees += is_prime(sum_tree(edge[0])) + is_prime(sum_tree(edge[1]))
        adj[edge[0]].add(edge[1])
        adj[edge[1]].add(edge[0])

    return prime_subtrees / len(edges)
