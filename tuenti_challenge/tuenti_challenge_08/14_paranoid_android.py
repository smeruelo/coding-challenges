#!/usr/bin/python3

from math import sqrt
from scipy.spatial import Voronoi
from scipy.sparse.csgraph import shortest_path, csgraph_from_dense
from numpy import array, inf

def distance(p1, p2):
    return sqrt(abs(p2[0] - p1[0]) ** 2 + abs(p2[1] - p1[1]) ** 2)

def nearest(p1, points):
    return min(map(lambda i, p2: (i, distance(p1, p2)), range(len(points)), points),
               key=lambda x: x[1])[0]

def distances_array(v, radius):
    l = []
    for _ in range(len(v.vertices)):
        l.append([inf] * len(v.vertices))
    a = array(l)

    for i, r in enumerate(v.ridge_vertices):
        s, t = r
        p1, p2 = v.ridge_points[i]
        if s != -1 and t != -1 and radius <= distance(v.points[p1], v.points[p2]) / 2:
            a[s][t] = a[t][s] = distance(v.vertices[s], v.vertices[t])
    return csgraph_from_dense(a, null_value=inf)

def shortest(points, radius, src, dest):
    v = Voronoi(points)
    begin = nearest(src, v.vertices)
    end = nearest(dest, v.vertices)
    path = distance(src, v.vertices[begin]) + distance(dest, v.vertices[end])
    distances = distances_array(v, radius)
    return path + shortest_path(distances)[begin][end]


if __name__ == '__main__':
    for i in range(int(input())):
        points = [list(map(int, input().split())) for _ in range(int(input()))]
        radius = eval(input())
        src = list(map(eval, input().split()))
        dest = list(map(eval, input().split()))
        length = shortest(points, radius, src, dest)
        if length == inf:
            print('Case #{}: IMPOSSIBLE'.format(i + 1))
        else:
            print('Case #{}: {}'.format(i + 1, "%.3f" % length))
