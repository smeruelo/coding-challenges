#!/usr/bin/python3
# https://www.codechef.com/WICP1901/problems/IPCTRAIN

# Partial solution only

import heapq


def min_sadness(days, data):
    total_sadness = 0
    trainers = []
    for day in range(1, days + 1):
        while data and data[-1][0] == day:
            arrival, lectures, sadness = data.pop()
            heapq.heappush(trainers, (-sadness, lectures))
            total_sadness += sadness * lectures
        if trainers:
            lecturer = trainers[0]
            total_sadness += lecturer[0]
            if lecturer[1] > 1:
                trainers[0] = (lecturer[0], lecturer[1] - 1)
            else:
                heapq.heappop(trainers)

    return total_sadness


for _ in range(int(input())):
    num_trainers, days = map(int, input().split())
    data = []
    for _ in range(num_trainers):
        data.append(tuple(map(int, input().split())))
    data.sort(reverse=True)
    print(min_sadness(days, data))
