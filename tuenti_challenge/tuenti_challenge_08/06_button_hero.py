#!/usr/bin/pypy3

import bisect

def events_needed(notes):
    def join_equals(events):
        joined = [events[0]]
        start_prev, end_prev, score_prev = events[0]
        for start_curr, end_curr, score_curr in events[1:]:
            if start_prev == start_curr and end_prev == end_curr:
                joined.pop()
                start_prev, end_prev, score_prev = start_curr, end_curr, score_prev + score_curr
            else:
                start_prev, end_prev, score_prev = start_curr, end_curr, score_curr
            joined.append((start_prev, end_prev, score_prev))
        return joined

    # tuples (push, release, score) ordered by release time
    events = [(x // s, (x + l) // s, p) for x, l, s, p in notes]
    events.sort(key=lambda x: x[0])
    events.sort(key=lambda x: x[1])
    return join_equals(events)

def max_score(notes):
    events = events_needed(notes)
    ends = list(map(lambda x: x[1], events))
    n = len(events)
    scores = [None] * (n + 1)
    scores[0] = 0

    def last(start):
        return bisect.bisect_left(ends, start)

    for i in range(1, n + 1):
        start, end, score = events[i - 1]
        scores[i] = max(scores[i - 1], scores[last(start)] + score)
    return scores[n]


if __name__ == '__main__':
    for i in range(int(input())):
        notes = [list(map(int, input().split())) for _ in range(int(input()))]
        print('Case #{}: {}'.format(i + 1, max_score(notes)))
