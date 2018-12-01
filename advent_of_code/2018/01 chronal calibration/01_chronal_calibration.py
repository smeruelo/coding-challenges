#!/usr/bin/python3
# https://adventofcode.com/2018/day/1

if __name__ == '__main__':
    # part 1
    with open('01_chronal_calibration.input') as f:
        changes = list(map(int, f.read().split('\n')))
    print(sum(changes))

    # part 2
    frequency = 0
    duplicated = False
    reached_frequencies = set()
    while not duplicated:
        for change in changes:
            frequency += change
            if frequency in reached_frequencies:
                duplicated = True
                break
            else:
                reached_frequencies.add(frequency)
    print(frequency)
