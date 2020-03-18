# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096


WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'
POINTS = {WIN: 3, DRAW: 1, LOSS: 0}


class Team():
    def __init__(self, name):
        self.name = name
        self.matches = {WIN: 0, DRAW: 0, LOSS: 0}

    def matches_played(self):
        return sum(self.matches.values())

    def points(self):
        return sum([POINTS[result] * count for result, count in self.matches.items()])

    def __lt__(self, other):
        if self.points() == other.points():
            return self.name > other.name
        else:
            return self.points() < other.points()

    def __str__(self):
        return (
            f'{self.name:30} | '
            f'{self.matches_played():2} | '
            f'{self.matches[WIN]:2} | '
            f'{self.matches[DRAW]:2} | '
            f'{self.matches[LOSS]:2} | '
            f'{self.points():2}'
        )


def tally(rows):

    def update_teams(teams, name, result):
        if name not in teams:
            teams[name] = Team(name)
        teams[name].matches[result] += 1
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
            table.append(str(team))
        return table

    return table(read_results(rows))
