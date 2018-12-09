#!/usr/bin/python3
# https://adventofcode.com/2018/day/8

def license1(data):
    def tree(i):
        num_children = data[i]
        num_metadata = data[i+1]
        sum_metadata = 0
        j = i + 2
        for child in range(num_children):
            j, metadata = tree(j)
            sum_metadata += metadata
        last = j + num_metadata
        sum_metadata += sum(data[j:last])
        return last, sum_metadata
    return tree(0)[1]

def license2(data):
    def tree(i):
        num_children = data[i]
        num_metadata = data[i+1]
        j = i + 2
        if num_children == 0:
            last = j + num_metadata
            return last, sum(data[j:last])
        else:
            children = [0] * (num_children + 1)
            value = 0
            for child in range(1, num_children + 1):
                j, v = tree(j)
                children[child] = v
            for md in range(num_metadata):
                child = data[j + md]
                if child <= num_children:
                    value += children[child]
            return j + num_metadata, value
    return tree(0)[1]


if __name__ == '__main__':
    with open('08_memory_maneuver.input') as f:
        data = list(map(int, f.read().split()))

    print(license1(data))
    print(license2(data))
