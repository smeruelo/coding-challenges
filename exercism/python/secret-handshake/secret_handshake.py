# https://exercism.io/my/solutions/17b4902ac9334076b4da2b91cfcf4f32

ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']


def commands(number):
    # Convert to binary, take the 5 less-significative bits (reversed)
    s = format(number, 'b')[::-1][:5]

    handshake = list(filter(lambda x: x,
                            map(lambda c, action: action if c == '1' else None, s, ACTIONS)))
    if len(s) == 5 and s[4] == '1':
        return handshake[::-1]
    else:
        return handshake
