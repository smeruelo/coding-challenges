// https://exercism.io/my/solutions/e783f2c3fde94fba9096cad8df62dd66

package etl

import "strings"

// Transform takes a translation table in the form points->(letter, letter, ..)
// and returns a new one in the form letter->points
func Transform(pointsOld map[int][]string) map[string]int {
	pointsNew := make(map[string]int)
	for k, v := range pointsOld {
		for _, letter := range v {
			pointsNew[strings.ToLower(letter)] = k
		}
	}
	return pointsNew
}
