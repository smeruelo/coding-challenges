#!/usr/bin/pypy
# https://www.hackerrank.com/contests/womenscup/challenges/antony-and-the-magical-pearls


from Queue import PriorityQueue


def cost(pearls):
    def sum_mod(a, b):
        return (a + b) % (pow(10, 9) + 7)

    pq = PriorityQueue()
    for i in pearls:
        pq.put(i)

    cost = 0
    while pq.qsize() > 1:
        new_pearl = sum_mod(pq.get(), pq.get())
        cost = sum_mod(cost, new_pearl)
        pq.put(new_pearl)
    return cost

if __name__ == '__main__':
    _ = raw_input()
    pearls = map(int, raw_input().split())
    print cost(pearls)
