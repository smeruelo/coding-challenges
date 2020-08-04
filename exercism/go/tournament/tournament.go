// https://exercism.io/my/solutions/9a68f3c1492f4922b0f5090f08966933

package tournament

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"sort"
	"strings"
)

type matchResult string

const (
	draw matchResult = "draw"
	loss matchResult = "loss"
	win  matchResult = "win"
)

var (
	points         = map[matchResult]int{draw: 1, loss: 0, win: 3}
	oppositeResult = map[matchResult]matchResult{draw: draw, loss: win, win: loss}
)

// team stores a team's matches' results
type team struct {
	matches int
	draws   int
	losses  int
	wins    int
	points  int
}

// readResults reads, validates and process the input data
func readResults(r io.Reader) (map[string]team, error) {
	teams := map[string]team{}
	s := bufio.NewScanner(r)

	for s.Scan() {
		if s.Text() == "" || s.Text()[0] == '#' {
			continue
		}
		matchInfo := strings.Split(s.Text(), ";")
		if len(matchInfo) != 3 {
			return teams, errors.New("invalid input")
		}
		nameTeam1, nameTeam2, r := matchInfo[0], matchInfo[1], matchInfo[2]
		result := matchResult(r)
		t1, t2 := teams[nameTeam1], teams[nameTeam2]

		switch result {
		case draw:
			t1.draws++
			t2.draws++
		case loss:
			t1.losses++
			t2.wins++
		case win:
			t1.wins++
			t2.losses++
		default:
			return teams, errors.New("invalid input")
		}
		t1.matches++
		t2.matches++
		t1.points += points[result]
		t2.points += points[oppositeResult[result]]
		teams[nameTeam1], teams[nameTeam2] = t1, t2
	}

	return teams, nil
}

// sortTeams provides a slice of team names, sorted by points and name
func sortTeams(teams map[string]team) []string {
	names := make([]string, len(teams))
	i := 0
	for k := range teams {
		names[i] = k
		i++
	}
	sort.Slice(names, func(i, j int) bool {
		pointsI := teams[names[i]].points
		pointsJ := teams[names[j]].points
		if pointsI > pointsJ {
			return true
		}
		if pointsI == pointsJ {
			return names[i] < names[j]
		}
		return false
	})
	return names
}

// Tally reads a series of matches results and pretty prints them
func Tally(r io.Reader, w io.Writer) error {
	teams, err := readResults(r)
	if err != nil {
		return err
	}

	bw := bufio.NewWriter(w)
	header := "Team                           | MP |  W |  D |  L |  P\n"
	bw.WriteString(header)

	teamRow := func(team string) string {
		results := teams[team]
		mp := results.matches
		w := results.wins
		d := results.draws
		l := results.losses
		p := results.points
		return fmt.Sprintf("%-30s | %2d | %2d | %2d | %2d | %2d\n", team, mp, w, d, l, p)
	}
	for _, team := range sortTeams(teams) {
		bw.WriteString(teamRow(team))
	}

	bw.Flush()
	return nil
}
