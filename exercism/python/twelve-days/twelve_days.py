#https://exercism.io/my/solutions/27c44b1163494641ac0470f4777858b6


def recite(start_verse, end_verse):

    DATA = [('first', 'a Partridge in a Pear Tree'),
            ('second', 'two Turtle Doves'),
            ('third', 'three French Hens'),
            ('fourth', 'four Calling Birds'),
            ('fifth', 'five Gold Rings'),
            ('sixth', 'six Geese-a-Laying'),
            ('seventh', 'seven Swans-a-Swimming'),
            ('eighth', 'eight Maids-a-Milking'),
            ('ninth', 'nine Ladies Dancing'),
            ('tenth', 'ten Lords-a-Leaping'),
            ('eleventh', 'eleven Pipers Piping'),
            ('twelfth', 'twelve Drummers Drumming')]

    def presents(d):
        last = DATA[0][1] if d == 1 else f', and {DATA[0][1]}'
        rest = ', '.join(DATA[j-1][1] for j in range(d, 1, -1))
        return rest + last

    def verse(d):
        return f'On the {DATA[d-1][0]} day of Christmas my true love gave to me: {presents(d)}.'

    return [verse(i) for i in range(start_verse, end_verse + 1)]
