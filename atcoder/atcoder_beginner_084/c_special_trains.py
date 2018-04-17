#!/usr/bin/python3
# https://abc084.contest.atcoder.jp/tasks/abc084_c

def min_times(stations, n):
    times = []
    for i in range(n - 1):
        ci, si, fi = stations[i]
        t = si + ci
        for j in range(i + 1, n - 1):
            cj, sj, fj = stations[j]
            if t < sj:
                t = sj + cj
            else:
                waiting = fj - (t - sj) % fj if (t - sj) % fj != 0 else 0
                t += waiting + cj
        times.append(t)
    times.append(0)
    return times


if __name__ == '__main__':
    n = int(input())
    stations = [list(map(int, input().split())) for _ in range(n - 1)]
    for i in min_times(stations, n):
        print(i)
