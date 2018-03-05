#!/usr/bin/python3

def solution(S, T):
    if S == T:
        return "NOTHING"
    if len(T) == len(S) + 1:
        for i in range(len(T)):
            if T[0:i] + T[i+1:] == S:
                return 'INSERT {}'.format(T[i])
    if len(T) == len(S) - 1:
        for i in range(len(S)):
            if S[0:i] + S[i+1:] == T:
                return 'DELETE {}'.format(S[i])
    if len(T) == len(S):
        for i in range(len(S) - 1):
            if S[0:i] + S[i+1] + S[i] + S[i+2:] == T:
                return 'SWAP {} {}'.format(S[i], S[i+1])
    return "IMPOSSIBLE"


if __name__ == '__main__':
    # Some tests
    print(solution('nice', 'niece'), 'INSERT e')
    print(solution('niece', 'nice'), 'DELETE e')
    print(solution('nice', 'nice'), 'NOTHING')
    print(solution('niec', 'nice'), 'SWAP e c')
    print(solution('aceite', 'agua'), 'IMPOSSIBLE')
    print(solution('x', 'x'), 'NOTHING')
    print(solution('nidepalo', 'no'), 'IMPOSSIBLE')
    print(solution('imposible', 'miposilbe'), 'IMPOSSIBLE')
    print(solution('nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobewmbwmbwm', 'nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobemwbwmbwm'), 'SWAP w m')
    print(solution('nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobewmbwmbwm', 'nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobemwbwmbwmr'), 'IMPOSSIBLE')
    print(solution('nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobewmbwmbwm', 'nthounthouentohuntohuntoheotunththbwbqjmjqwjqkbwmkjqbjbmqkjbmkmwboewmwmaoawwewmobeuwmbwmobiewmbwmbwm'), 'INSERT i')
