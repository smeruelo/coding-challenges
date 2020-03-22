# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096


WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'
RESULTS = {WIN, DRAW, LOSS}
POINTS = {WIN: 3, DRAW: 1, LOSS: 0}


class Team():
    def __init__(self, name):
        self._name = name
        self._matches = {WIN: 0, DRAW: 0, LOSS: 0}

    @property
    def name(self):
        return self._name

    def matches(self, result):
        if result not in RESULTS:
            raise ValueError('Result must be "win", "draw", or "loss"')
        return self._matches[result]

    def add_result(self, result):
        if result not in RESULTS:
            raise ValueError('Result must be "win", "draw", or "loss"')
        self._matches[result] += 1

    @property
    def matches_played(self):
        return sum(self._matches.values())

    @property
    def points(self):
        return sum([POINTS[result] * count for result, count in self._matches.items()])

    def __lt__(self, other):
        if self.points == other.points:
            return self.name > other.name
        else:
            return self.points < other.points


def tally(rows):

    def update_teams(teams, name, result):
        if name not in teams:
            teams[name] = Team(name)
        teams[name].add_result(result)
        return

    def read_results(rows):
        other_team_result = {WIN:LOSS, DRAW:DRAW, LOSS:WIN}
        teams = dict()
        for row in rows:
            team1, team2, result = row.split(';')
            update_teams(teams, team1, result)
            update_teams(teams, team2, other_team_result[result])
        return teams

    def table(teams):
        table = ['Team                           | MP |  W |  D |  L |  P']
        for team in sorted(teams.values(), reverse=True):
            row = (
                f'{team.name:30} | '
                f'{team.matches_played:2} | '
                f'{team.matches(WIN):2} | '
                f'{team.matches(DRAW):2} | '
                f'{team.matches(LOSS):2} | '
                f'{team.points:2}'
            )
            table.append(row)
        return table

    return table(read_results(rows))
