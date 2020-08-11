// https://exercism.io/my/solutions/7aa7eb5ea75141f7a7979c12b0e5c212

package cryptosquare

import (
	"math"
	"strings"
	"unicode"
)

func normalize(s string) string {
	alphanumToLower := func(r rune) rune {
		if !unicode.IsLetter(r) && !unicode.IsDigit(r) {
			return -1
		}
		return unicode.ToLower(r)
	}

	return strings.Map(alphanumToLower, s)
}

func dimensions(n int) (int, int) {
	height := int(math.Round(math.Sqrt(float64(n))))
	var width int
	if height*height == n {
		width = height
	} else {
		width = int(math.Floor(math.Sqrt(float64(n)))) + 1
	}
	return height, width
}

// Encode encodes a string using a cryptosquare
func Encode(s string) string {
	plain := []rune(normalize(s))
	n := len(plain)
	h, w := dimensions(n)
	square := make([][]rune, h)

	for r := 0; r < h; r++ {
		row := make([]rune, w)
		for c := 0; c < w; c++ {
			index := (r * w) + c
			if index >= n {
				row[c] = ' '
			} else {
				row[c] = plain[index]
			}
		}
		square[r] = row
	}

	var b strings.Builder
	for c := 0; c < w; c++ {
		for r := 0; r < h; r++ {
			b.WriteRune(square[r][c])
		}
		if c != w-1 {
			b.WriteRune(' ')
		}
	}
	return b.String()
}
