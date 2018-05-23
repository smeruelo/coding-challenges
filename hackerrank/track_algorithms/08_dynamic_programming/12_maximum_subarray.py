#!/usr/bin/python3
# https://www.hackerrank.com/challenges/maxsubarray/problem

def biggest_subs(n, array):
    sums_arrays = [0]
    sums_sequences = [0]
    maximum = array[0]
    for i in array:
        maximum = max(i, maximum)
        sums_arrays.append(max(sums_arrays[-1] + i, i))
        sums_sequences.append(max(sums_sequences[-1] + i, sums_sequences[-1]))

    if maximum < 0:
        return [max(sums_arrays[1:]), maximum]
    else:
        return [max(sums_arrays[1:]), max(sums_sequences[1:])]


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        array = list(map(int, input().split()))
        print(' '.join(map(str, biggest_subs(n, array))))
