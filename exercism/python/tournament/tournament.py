# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096

from collections import namedtuple

WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'

TeamData = namedtuple('TeamData', ['won', 'drawn', 'lost', 'points'], defaults=(0, 0, 0, 0))


def tally(rows):

    def add_team_result(data, team, result):
        current = data[team] if team in data else TeamData()
        if result == WIN:
            data[team] = TeamData(current.won + 1, current.drawn, current.lost, current.points + WIN_POINTS)
        elif result == DRAW:
            data[team] = TeamData(current.won, current.drawn + 1, current.lost, current.points + DRAW_POINTS)
        elif result == LOSS:
            data[team] = TeamData(current.won, current.drawn, current.lost + 1, current.points + LOSS_POINTS)
        return

    def read_results(rows):
        other_team_result = {WIN:LOSS, DRAW:DRAW, LOSS:WIN}
        data = dict()
        for row in rows:
            team1, team2, result = row.split(';')
            add_team_result(data, team1, result)
            add_team_result(data, team2, other_team_result[result])
        return data

    def table(data):
        def points_descending_name_ascending(team_and_data):
            name, data = team_and_data
            return (-data.points, name)

        table = ['Team                           | MP |  W |  D |  L |  P']
        for team, team_data in sorted(data.items(), key=points_descending_name_ascending):
            won, drawn, lost, points = team_data
            played = won + drawn + lost
            table.append(f'{team:30} | {played:2} | {won:2} | {drawn:2} | {lost:2} | {points:2}')
        return table

    return table(read_results(rows))
