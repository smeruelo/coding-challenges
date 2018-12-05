#!/usr/bin/python3
# https://adventofcode.com/2018/day/4

from datetime import datetime
from collections import defaultdict


def sort_data(data):
    parsed_data = []
    for line in data:
        d, info = line.split('] ')
        date = datetime.strptime(d, '[%Y-%m-%d %H:%M')
        parsed_data.append((date, info))
    return sorted(parsed_data)

def process_log(log):
    sleep_times = defaultdict(lambda: [0] * 60)
    guard_id = -1
    i = 0
    while i in range(len(log)):
        date, info = log[i]
        if info.startswith("Guard"):
            guard_id = int(info.split('#')[1].split()[0])
            i += 1
        else:
            asleep = date.minute
            awake = log[i+1][0].minute
            for j in range(asleep, awake):
                sleep_times[guard_id][j] += 1
            i += 2
    return sleep_times


if __name__ == '__main__':
    with open('04_repose_record.input') as f:
        log = sort_data(f.read().split('\n'))
    sleep_times = process_log(log)

    # part 1
    guard_id = max(sleep_times, key=lambda k: sum(sleep_times[k]))
    minute = sorted(enumerate(sleep_times[guard_id]), key=lambda x: x[1])[59][0]
    print(guard_id * minute)

    # part 2
    guard_id = max(sleep_times, key=lambda k: max(sleep_times[k]))
    minute = sorted(enumerate(sleep_times[guard_id]), key=lambda x: x[1])[59][0]
    print(guard_id * minute)
