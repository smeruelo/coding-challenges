// https://exercism.io/my/solutions/69c9306699e043cdb29d1993bc35e68a

package isbn

import "unicode"

func digit(index int, char rune) (int, bool) {
	if unicode.IsDigit(char) && index <= 9 {
		return int(char - '0'), true
	}
	if (char == 'x' || char == 'X') && index == 9 {
		return 10, true
	}
	return -1, false
}

func IsValidISBN(s string) bool {
	isbn := [10]int{}

	j := 0
	checksum := 0
	for _, r := range s {
		if r == '-' {
			continue
		}
		d, ok := digit(j, r)
		if !ok {
			return false
		}
		isbn[j] = d
		checksum += (10 - j) * d
		j++
	}
	if j < 10 {
		return false
	}
	return checksum%11 == 0
}
