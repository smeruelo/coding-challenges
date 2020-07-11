// https://exercism.io/my/solutions/e783f2c3fde94fba9096cad8df62dd66

package etl

import "strings"

// Transform takes a translation table in the form points->(letter, letter, ..)
// and returns a new one in the form letter->points
func Transform(scoreOld map[int][]string) map[string]int {
	scoreNew := make(map[string]int)
	for points, letters := range scoreOld {
		for _, letter := range letters {
			scoreNew[strings.ToLower(letter)] = points
		}
	}
	return scoreNew
}
