# https://exercism.io/my/solutions/33639bd3816c4af892309fb95f88f1c8

def recite(start_verse, end_verse):
    who = ['house',
           'malt',
           'rat',
           'cat',
           'dog',
           'cow with the crumpled horn',
           'maiden all forlorn',
           'man all tattered and torn',
           'priest all shaven and shorn',
           'rooster that crowed in the morn',
           'farmer sowing his corn',
           'horse and the hound and the horn']

    what = ['Jack built',
            'lay in',
            'ate',
            'killed',
            'worried',
            'tossed',
            'milked',
            'kissed',
            'married',
            'woke',
            'kept',
            'belonged to']

    def verse(i):
        s = 'This is'
        for j in range(i-1, -1, -1):
            s += f' the {who[j]} that {what[j]}'
        return f'{s}.'

    output = []
    for i in range(start_verse, end_verse+1):
        output.append(verse(i))
    return output
