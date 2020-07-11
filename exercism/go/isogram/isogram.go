// https://exercism.io/my/solutions/747fe2ed9a704505a22508d80525ef25

package isogram

import (
	"unicode"
)

// IsIsogram determines whether a text is an isogram or not
func IsIsogram(text string) bool {
	appearsInText := make(map[rune]bool)
	for _, c := range text {
		if !unicode.IsLetter(c) {
			continue
		}
		c = unicode.ToLower(c)
		if appearsInText[c] {
			return false
		}
		appearsInText[c] = true
	}
	return true
}
