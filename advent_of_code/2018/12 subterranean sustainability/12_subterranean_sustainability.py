#!/usr/bin/python3
# https://adventofcode.com/2018/day/12

def parse_data(data):
    initial_state = data[0].split()[2]
    notes = dict()
    for i in range(2, len(data)):
        aux = data[i].split()
        notes[aux[0]] = aux[2]
    return (initial_state, notes)

def five(state, i):
    begin = i - 2
    end = i + 2
    if begin < 0:
        five = '.' * abs(begin) + state[0:5+begin]
    elif end >= len(state):
        five = state[end-4:] + '.' * (end - len(state) + 1)
    else:
        five = state[begin:end+1]
    return five

def next_generation(state, notes, offset):
    s = '..' + state + '..'
    new_state = ''
    for i in range(len(s)):
        new_state = new_state + notes[five(s, i)]
    first = new_state.find('#')
    last = len(new_state) - 1 - new_state[::-1].find('#')
    new_offset = offset + 2 - first
    return new_state[first:last+1], new_offset

def sum_numbers(state, offset):
    numbers = map(lambda i, pot: i - offset if pot == '#' else 0, range(len(state)), state)
    return sum(numbers)


if __name__ == '__main__':
    with open('12_subterranean_sustainability.input') as f:
        data = list(f.read().split('\n'))
    initial_state, notes = parse_data(data)

    # part 1
    state = initial_state
    offset = 0
    for i in range(20):
        state, offset = next_generation(state, notes, offset)
        # print('%4s' % str(i+1) + ' ' + ' ' * (-offset) + state)
    print(sum_numbers(state, offset))

    # part 2
    # Repeating previous loop for bigger range, we see that from generation 91 on, output is the
    # same but moving itself one pot to the right (actually, to the left)
    state = initial_state
    offset = 0
    for i in range(91):
        state, offset = next_generation(state, notes, offset)
    state91, offset91 = state, offset
    offset50000000000 = offset91 + 91 - 50000000000
    print(sum_numbers(state91, offset50000000000))
