# https://exercism.io/my/solutions/b3b91870e23c4ca7ae4ea6661ece1096

WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'


def tally(rows):

    def add_team_result(data, team, result):
        if team in data:
            w, d, l, p = data[team]
        else:
            w, d, l, p = 0, 0, 0, 0
        if result == WIN:
            data[team] = (w + 1, d, l, p + WIN_POINTS)
        elif result == DRAW:
            data[team] = (w, d + 1, l, p + DRAW_POINTS)
        elif result == LOSS:
            data[team] = (w, d, l + 1, p + LOSS_POINTS)
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
        table = ['Team                           | MP |  W |  D |  L |  P']
        for team, team_data in sorted(data.items(), key=lambda x: (-x[1][3], x[0])):
            w, d, l, p = team_data
            mp = w + d + l
            table.append(f'{team:30} | {mp:2} | {w:2} | {d:2} | {l:2} | {p:2}')
        return table

    return table(read_results(rows))
