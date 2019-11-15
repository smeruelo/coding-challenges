# https://exercism.io/my/solutions/17b4902ac9334076b4da2b91cfcf4f32

ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']


def commands(number):
    s = format(number, 'b')[::-1]
    handshake = [ACTIONS[i] for i, bit in enumerate(s[:4]) if bit == '1']
    return handshake[::-1] if len(s) > 4 and s[4] == '1' else handshake
