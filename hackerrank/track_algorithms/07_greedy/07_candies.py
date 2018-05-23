#!/usr/bin/python3
# https://www.hackerrank.com/challenges/candies/problem

def candies(ratings):
    def aux(l):
        out = [1]
        prev = l[0]
        i = 1
        while i < len(l):
            curr = l[i]
            if curr > prev:
                out.append(out[-1] + 1)
            else:
                out.append(1)
            i += 1
            prev = curr
        return out

    forward = aux(ratings)
    backwards = reversed(aux(ratings[::-1]))
    return sum(map(lambda x, y: max(x, y), forward, backwards))


if __name__ == '__main__':
    ratings = [int(input()) for _ in range(int(input()))]
    print(candies(ratings))
