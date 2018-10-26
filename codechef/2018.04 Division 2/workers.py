#!/usr/bin/python3
# https://www.codechef.com/APRIL18B/problems/CHEFWORK

TRANSLATOR = '1'
AUTHOR = '2'
AUTHOR_TRANSLATOR = '3'

def min_cost(costs, types):
    zipped = list(zip(costs, types))

    def min_cost_of_type(worker_type):
        tuples_filtered = list(filter(lambda x: x[1] == worker_type, zipped))
        if tuples_filtered:
            costs, types = zip(*tuples_filtered)
            return min(costs)
        else:
            return None

    min_author_translator = min_cost_of_type(AUTHOR_TRANSLATOR)
    min_author = min_cost_of_type(AUTHOR)
    min_translator = min_cost_of_type(TRANSLATOR)

    if min_author_translator:
        if min_author and min_translator:
            return min(min_author_translator, min_author + min_translator)
        else:
            return min_author_translator
    else:
        return min_author + min_translator


if __name__ == '__main__':
    n = input()
    costs = list(map(int, input().split()))
    types = input().split()
    print(min_cost(costs, types))
