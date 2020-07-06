// https://exercism.io/my/solutions/f8101846681f43b18f9abee5cb4cd092

package scrabble

import (
	"strings"
)

var points = map[rune]int{
	'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
	'd': 2, 'g': 2,
	'b': 3, 'c': 3, 'm': 3, 'p': 3,
	'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
	'k': 5,
	'j': 8, 'x': 8,
	'q': 10, 'z': 10,
}

// Score returns the total scrabble score for a given word
func Score(word string) int {
	var score = 0
	for _, letter := range strings.ToLower(word) {
		score += points[letter]
	}
	return score
}
