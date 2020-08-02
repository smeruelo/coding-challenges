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

// teamResults stores how many matches has a team won/drawn/lost
type teamResults map[matchResult]int

func (tr teamResults) add(result matchResult) {
	tr[result]++
}

// matchesPlayed returns the total number of matches played by a team
func (tr teamResults) matchesPlayed() int {
	return tr[draw] + tr[loss] + tr[win]
}

// points returns the total number of points obtained by a team
func (tr teamResults) points() int {
	return tr[draw]*points[draw] + tr[loss]*points[loss] + tr[win]*points[win]
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
			teams[nameTeam1] = teamResults{}
		}
		teams[nameTeam1].add(result)
		if _, ok := teams[nameTeam2]; !ok {
			teams[nameTeam2] = teamResults{}
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
		w := results[win]
		d := results[draw]
		l := results[loss]
		p := results.points()
		return fmt.Sprintf("%-30s | %2d | %2d | %2d | %2d | %2d\n", team, mp, w, d, l, p)
	}
	for _, team := range sortTeams(teams) {
		bw.WriteString(teamRow(team))
	}

	bw.Flush()
	return nil
}
