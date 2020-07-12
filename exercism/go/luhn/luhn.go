// https://exercism.io/my/solutions/f2b3c9c4dc674ba4974f802c22679862

package luhn

import (
	"strings"
	"unicode"
)

func runeToInt(r rune) int {
	return int(r) - '0'
}

// Valid determines whether a series of digits is valid or not, according to Luhn algorithm
func Valid(s string) bool {
	s = strings.ReplaceAll(s, " ", "")
	if len(s) <= 1 {
		return false
	}

	// In odd-length strings, odd-position digits will be doubled
	// In even-length strings, the even-position ones
	parity := len(s) % 2
	sum := 0
	for i, char := range s {
		if !unicode.IsNumber(char) {
			return false
		}
		addend := runeToInt(char)
		if i%2 == parity {
			addend *= 2
			if addend >= 9 {
				addend -= 9
			}
		}
		sum += addend
	}
	return sum%10 == 0
}
