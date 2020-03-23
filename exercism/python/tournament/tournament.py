# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096


WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'
RESULTS = {WIN, DRAW, LOSS}
POINTS = {WIN: 3, DRAW: 1, LOSS: 0}


class Team():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def add_result(self, result):
        if result not in RESULTS:
            raise ValueError(f'Result must be one of {RESULTS}')
        if result == WIN:
            self.wins += 1
        elif result == LOSS:
            self.losses += 1
        else:
            self.draws += 1

    @property
    def matches_played(self):
        return self.wins + self.losses + self.draws

    @property
    def points(self):
        return self.wins * POINTS[WIN] + self.losses * POINTS[LOSS] + self.draws * POINTS[DRAW]

    def __lt__(self, other):
        if self.points == other.points:
            return self.name > other.name
        else:
            return self.points < other.points


def tally(rows):

    def read_results(rows):
        other_team_result = {WIN: LOSS, DRAW: DRAW, LOSS: WIN}
        teams = dict()
        for row in rows:
            name1, name2, result1 = row.split(';')
            result2 = other_team_result[result1]
            team1 = teams.setdefault(name1, Team(name1))
            team2 = teams.setdefault(name2, Team(name2))
            team1.add_result(result1)
            team2.add_result(result2)
        return teams

    def table(teams):
        table = ['Team                           | MP |  W |  D |  L |  P']
        for team in sorted(teams.values(), reverse=True):
            row = (
                f'{team.name:30} | '
                f'{team.matches_played:2} | '
                f'{team.wins:2} | '
                f'{team.draws:2} | '
                f'{team.losses:2} | '
                f'{team.points:2}'
            )
            table.append(row)
        return table

    return table(read_results(rows))
