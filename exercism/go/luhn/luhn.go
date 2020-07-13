// https://exercism.io/my/solutions/f2b3c9c4dc674ba4974f802c22679862

package luhn

import (
	"strings"
	"unicode"
)

// Valid determines whether a series of digits is valid or not, according to Luhn algorithm
func Valid(s string) bool {
	s = strings.ReplaceAll(s, " ", "")
	if len(s) <= 1 {
		return false
	}

	// In even-length strings, we start by doubling the first digit
	mustDouble := len(s)%2 == 0
	sum := 0
	for _, char := range s {
		if !unicode.IsNumber(char) {
			return false
		}
		digit := int(char) - '0'
		if mustDouble {
			digit *= 2
			if digit > 9 {
				digit -= 9
			}
			mustDouble = false
		} else {
			mustDouble = true
		}
		sum += digit
	}
	return sum%10 == 0
}
