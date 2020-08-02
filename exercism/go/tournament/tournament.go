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

// teamResults stores how many matches has a team won/drawn/lost
type teamResults struct {
	matches map[matchResult]int
}

func newTeamResults() teamResults {
	return teamResults{matches: map[matchResult]int{}}
}

func (t teamResults) add(result matchResult) {
	t.matches[result]++
}

// matchesPlayed returns the total number of matches played by a team
func (t teamResults) matchesPlayed() int {
	return t.matches[draw] + t.matches[loss] + t.matches[win]
}

// points returns the total number of points obtained by a team
func (t teamResults) points() int {
	return t.matches[draw]*points[draw] +
		t.matches[loss]*points[loss] +
		t.matches[win]*points[win]
}

// readResults reads, validates and process the input data
func readResults(r io.Reader) (map[string]teamResults, error) {
	teams := map[string]teamResults{}
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
		if result != draw && result != loss && result != win {
			return teams, errors.New("invalid input")
		}
		if _, ok := teams[nameTeam1]; !ok {
			teams[nameTeam1] = newTeamResults()
		}
		teams[nameTeam1].add(result)
		if _, ok := teams[nameTeam2]; !ok {
			teams[nameTeam2] = newTeamResults()
		}
		teams[nameTeam2].add(oppositeResult[result])
	}
	return teams, nil
}

// sortTeams provides a slice of team names, sorted by points and name
func sortTeams(teams map[string]teamResults) []string {
	names := make([]string, len(teams))
	i := 0
	for k := range teams {
		names[i] = k
		i++
	}
	sort.Slice(names, func(i, j int) bool {
		pointsI := teams[names[i]].points()
		pointsJ := teams[names[j]].points()
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
		mp := results.matchesPlayed()
		w := results.matches[win]
		d := results.matches[draw]
		l := results.matches[loss]
		p := results.points()
		return fmt.Sprintf("%-30s | %2d | %2d | %2d | %2d | %2d\n", team, mp, w, d, l, p)
	}
	for _, team := range sortTeams(teams) {
		bw.WriteString(teamRow(team))
	}

	bw.Flush()
	return nil
}
