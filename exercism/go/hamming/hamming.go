// https://exercism.io/my/solutions/36b1acdbd9904bee98ee2497b37d1861

// Package hamming provides cool DNA-related tools.
package hamming

import (
	"errors"
)

// Distance returns the Hamming distance among two strings.
func Distance(s1, s2 string) (int, error) {
	r1 := []rune(s1)
	r2 := []rune(s2)

	if len(r1) != len(r2) {
		return 0, errors.New("strings have different length")
	}

	distance := 0
	for i := 0; i < len(r1); i++ {
		if r1[i] != r2[i] {
			distance++
		}
	}
	return distance, nil
}
