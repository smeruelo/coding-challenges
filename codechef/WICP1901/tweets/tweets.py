#!/usr/bin/python3
# https://www.codechef.com/WICP1901/problems/TWTCLOSE


t, c = map(int, input().split())
tweets = [False] * (t + 1)

for _ in range(c):
    click = input().split()
    if click[0] == 'CLICK':
        tweet = int(click[1])
        tweets[tweet] = not tweets[tweet]
        print(sum(tweets))
    else:
        tweets = [False] * (t + 1)
        print(0)
