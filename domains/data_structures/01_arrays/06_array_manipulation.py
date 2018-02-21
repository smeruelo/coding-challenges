#!/usr/bin/python2
# https://www.hackerrank.com/challenges/crush/problem

# https://wcipeg.com/wiki/Prefix_sum_array_and_difference_array

def calc_array(diff_arr):
    # Calculates the actual values from a difference array
    arr = [0] * n
    current = 0
    for i in xrange(len(diff_arr)):
        current += diff_arr[i]
        arr[i] = current
    return arr


if __name__ == '__main__':
    n, m = map(int, raw_input().split())

    diff_arr = [0] * n
    for _ in xrange(m):
        a, b, k =  map(int, raw_input().split())
        diff_arr[a - 1] += k
        if b < len(diff_arr):
            diff_arr[b] -= k

    print max(calc_array(diff_arr))
