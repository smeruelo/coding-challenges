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

// team stores a team's matches' results
type team struct {
	name    string
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
		line := s.Text()
		if line == "" || strings.HasPrefix(line, "#") {
			continue
		}
		matchInfo := strings.Split(line, ";")
		if len(matchInfo) != 3 {
			return teams, fmt.Errorf("invalid format %q (expected: 'team1;team2;result')", line)
		}
		nameTeam1, nameTeam2, result := matchInfo[0], matchInfo[1], matchInfo[2]
		t1, t2 := teams[nameTeam1], teams[nameTeam2]

		switch result {
		case "draw":
			t1.draws++
			t2.draws++
			t1.points++
			t2.points++
		case "loss":
			t1.losses++
			t2.wins++
			t2.points += 3
		case "win":
			t1.wins++
			t2.losses++
			t1.points += 3
		default:
			return teams, errors.New("invalid input")
		}
		t1.matches++
		t2.matches++
		t1.name = nameTeam1
		t2.name = nameTeam2
		teams[nameTeam1], teams[nameTeam2] = t1, t2
	}

	return teams, nil
}

// sortTeams provides a slice of teams, sorted by points and name
func sortTeams(teams map[string]team) []team {
	s := make([]team, 0, len(teams))
	for _, t := range teams {
		s = append(s, t)
	}
	sort.Slice(s, func(i, j int) bool {
		if s[i].points == s[j].points {
			return s[i].name < s[j].name
		}
		return s[i].points > s[j].points
	})
	return s
}

// Tally reads a series of matches results and pretty prints them
func Tally(reader io.Reader, writer io.Writer) error {
	teams, err := readResults(reader)
	if err != nil {
		return err
	}

	header := "Team                           | MP |  W |  D |  L |  P\n"
	fmt.Fprintf(writer, header)
	for _, t := range sortTeams(teams) {
		name := t.name
		mp := t.matches
		w := t.wins
		d := t.draws
		l := t.losses
		p := t.points
		fmt.Fprintf(writer, "%-30s | %2d | %2d | %2d | %2d | %2d\n", name, mp, w, d, l, p)
	}

	return nil
}
