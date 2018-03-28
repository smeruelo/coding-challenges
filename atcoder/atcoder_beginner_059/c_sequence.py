#!/usr/bin/python3
# https://abc059.contest.atcoder.jp/tasks/arc072_a

def ops_needed(x, target):
    if abs(target - x) < abs(x):
        return 0
    else:
        return target - x

def count_ops(a, first_target):
    total_ops = 0
    accum = 0
    for i, ai in enumerate(a):
        new_accum = accum + a[i]
        if i % 2 == 1:
            ops = ops_needed(new_accum, first_target)
        else:
            ops = ops_needed(new_accum, -1 * first_target)
        total_ops += abs(ops)
        accum = new_accum + ops
    return total_ops


if __name__ == '__main__':
    _ = int(input())
    a = list(map(int, input().split()))
    print(min(count_ops(a, 1), count_ops(a, -1)))
