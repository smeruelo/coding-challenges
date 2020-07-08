// https://exercism.io/my/solutions/81a20055ff42466e8c3ee293fd377ae4

package romannumerals

import (
	"errors"
	"strconv"
	"strings"
)

// maxInt receives two integers and returns the bigger one
func maxInt(x int, y int) int {
	if x >= y {
		return x
	}
	return y
}

// Letters to represent 1 and 5, in the different 10-powers
// i.e. for 10^2, the 1 (100) is C, the 5 (500) is D
var ivLetters = map[int]string{0: "IV", 1: "XL", 2: "CD", 3: "MV"}

// Returns the roman representation of (only) one arabic digit, according to its ten-power
func digitToRoman(digit int, power int) string {
	one, five := string(ivLetters[power][0]), string(ivLetters[power][1])
	if digit < 4 {
		return strings.Repeat(one, digit)
	}
	if digit < 9 {
		return strings.Repeat(one, maxInt(5-digit, 0)) + // possible one before the V
			five +
			strings.Repeat(one, maxInt(digit-5, 0)) // possible ones after the V
	}
	return one + string(ivLetters[power+1][0]) // char corresponding to next ten-power is needed
}

// ToRomanNumeral returns the roman representation of an arabic number among (0, 3000]
func ToRomanNumeral(arabic int) (string, error) {
	if arabic <= 0 || arabic > 3000 {
		return "", errors.New("number is not positive or it's too big")
	}
	arabicStr := strconv.Itoa(arabic)
	roman := ""
	for i, digit := range arabicStr {
		power := len(arabicStr) - 1 - i
		roman += digitToRoman(int(digit-'0'), power)
	}
	return roman, nil
}
