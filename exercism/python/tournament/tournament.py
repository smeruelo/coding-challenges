# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096

from collections import namedtuple

WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'


class Team():
    def __init__(self, name):
        self.name = name
        self.won = 0
        self.drawn = 0
        self.lost = 0

    def matches_played(self):
        return self.won + self.drawn + self.lost

    def points(self):
        return self.won * WIN_POINTS + self.drawn * DRAW_POINTS + self.lost * LOSS_POINTS

    def __lt__(self, other):
        if self.points() == other.points():
            return self.name > other.name
        else:
            return self.points() < other.points()


def tally(rows):

    def update_teams(teams, name, result):
        if name not in teams:
            teams[name] = Team(name)
        team = teams[name]
        if result == WIN:
            team.won += 1
        elif result == DRAW:
            team.drawn += 1
        elif result == LOSS:
            team.lost += 1
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
            matches_played = team.matches_played()
            points = team.points()
            row = (
                f'{team.name:30} | {matches_played:2} | {team.won:2} | '
                f'{team.drawn:2} | {team.lost:2} | {points:2}'
            )
            table.append(row)
        return table

    return table(read_results(rows))
